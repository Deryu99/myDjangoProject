""" 
    from ../myDjangoProject/urls.py 
    from . (current directory) import views
"""
from django.urls import path
from . import views

""" 
    - View that runs when we go to '...', in this case views.home, views.impressum, etc.
    - name='' specifies path for this view
"""
urlpatterns = [
    path('', views.index, name='todoList-index'),
    path('add_todo/', views.add_todo, name='todoList-addTodo'),
    path('how_to_edit_todo/', views.how_to_edit_todo, name='todoList-howToEditTodo'),
    path('impressum/', views.impressum, name='todoList-impressum')
]
