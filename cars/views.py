from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .forms import CarForm
from django.contrib import messages

def cars(request):
    cars = Car.objects.order_by('-created_date')  # Add ordering
    paginator = Paginator(cars, 3)  # Show 3 cars per page
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car added successfully!')
            return redirect('cars')
    else:
        form = CarForm()
    
    context = {
        'cars': paged_cars,
        'form': form,
        'model_search': Car.objects.values_list('model', flat=True).distinct(),
        'city_search': Car.objects.values_list('city', flat=True).distinct(),
        'year_search': Car.objects.values_list('year', flat=True).distinct(),
        'body_style_search': Car.objects.values_list('body_style', flat=True).distinct(),
    }
    return render(request, 'cars/cars.html', context)

def car_detail(request, id):
    try:
        single_car = get_object_or_404(Car, pk=id)
        
        # Get related cars (same model, excluding current car)
        related_cars = Car.objects.filter(model=single_car.model).exclude(id=id)[:3]
        
        data = {
            'single_car': single_car,
            'related_cars': related_cars,
            'features': single_car.features.split(',') if single_car.features else [],
        }
        return render(request, 'cars/car_detail.html', data)
    except Exception as e:
        messages.error(request, f'Error loading car details: {str(e)}')
        return redirect('cars')

def search(request):
    cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'cars/search.html', data)

def inquiry(request):
    if request.method == "POST":
       
        return HttpResponse("Inquiry submitted")
    return redirect('/')

def update_car(request, id):
    car = Car.objects.get(Car, pk=id)
    form = CarForm(instance=car)

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car updated successfully!')
            return redirect('cars')
    context = {
        'form': form,
    }
    return render(request, 'cars/update_car.html', context = context)

def delete_car(request, id):
    car = Car.objects.get(pk=id)
    if request.method == 'POST':
        car.delete()
        return redirect('cars')
        messages.success(request, 'Car deleted successfully!')
    return render(request, 'cars/delete_car.html', {'car': car})    