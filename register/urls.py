from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('username_check/', views.username_check, name='username_check'),
    path('email_check/', views.email_check, name='email_check'),
]
