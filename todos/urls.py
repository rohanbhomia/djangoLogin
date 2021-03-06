from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('create_todo', views.create_todo, name='create_todo'),
    path('delete_todo', views.delete_todo, name='delete_todo'),
    path('edit_todo', views.edit_todo, name='edit_todo'),
    path('todo_list', views.todo_list, name='todo_list'),
    path('todo_list_json', views.todo_list_json.as_view(), name='todo_list_json'),
]
