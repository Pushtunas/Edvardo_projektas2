from django.urls import path
from .import views
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.profile, name='update'),
]
