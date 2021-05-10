""" 
    from ../myDjangoProject/urls.py 
    from . (current directory) import views
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todoList-index'),
    path('delete_todoItem/<int:pk>', views.delete_todoItem, name='todoList-indexDelete'),
    path('add_todo/', views.add_todo, name='todoList-addTodo'),
    path('how_to_edit_todo/', views.how_to_edit_todo, name='todoList-howToEditTodo'),
    path('impressum/', views.impressum, name='todoList-impressum')
]