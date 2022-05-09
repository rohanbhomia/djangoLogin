from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout')
]