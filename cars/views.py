from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .forms import CarForm
from django.contrib import messages

# Create your views here.
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
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)

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
        # Handle form logic here
        return HttpResponse("Inquiry submitted")
    return redirect('/')