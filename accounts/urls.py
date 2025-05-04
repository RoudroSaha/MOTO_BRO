from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Use your custom login view
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
