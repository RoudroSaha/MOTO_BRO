from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('cars/', views.cars, name='cars'),
    path('search/', views.search, name='search'),

    
    
     
    
]
 