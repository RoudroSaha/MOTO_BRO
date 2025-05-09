from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
    path('inquiry/', views.inquiry, name='inquiry'),
     path('add/', views.add_car, name='add_car'),
    path('update/<int:pk>/', views.update_car, name='update_car'),
    path('delete/<int:id>/', views.delete_car, name='delete_car'),

]