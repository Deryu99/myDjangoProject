from django.urls import path    #from ../myDjangoProject/urls.py
from . import views             #from . (current directory) import views

urlpatterns = [
    path('', views.index, name='todoList-index'),
    path('delete_todo/<int:pk>/', views.delete_todo , name='delete-todo'),
    path('edit_todo/<int:pk>/', views.edit_todo , name='edit-todo'),
    path('add_todo/', views.add_todo, name='todoList-addTodo'),
    path('how_to_edit_todo/', views.how_to_edit_todo, name='todoList-howToEditTodo'),
    path('impressum/', views.impressum, name='todoList-impressum')
]