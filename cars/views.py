from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CarForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    
    data = {
        'cars': paged_cars,
    }
    return render(request, 'cars/cars.html', data)

def update_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars')  # or wherever you want to redirect after update
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/update_car.html', {'form': form})

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

    data = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/search.html', data)

def inquiry(request):
    if request.method == 'POST':
        # Handle the inquiry form submission
        # You can add more logic here to process the inquiry
        return HttpResponse("Inquiry submitted successfully")
    return redirect('cars')


def delete_car(request, id):
    car = get_object_or_404(Car, pk=id)
    if request.method == 'POST':
        car.delete()
        return redirect('cars')
    return render(request, 'cars/delete_car.html', {'car': car})



@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            messages.success(request, 'Car added successfully!')
            return redirect('cars')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CarForm()
    return render(request, 'cars/add_car.html', {'form': form})

