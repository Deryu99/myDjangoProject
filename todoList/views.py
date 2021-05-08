from django.shortcuts import render
from django.http import HttpResponse

# dummy todos
todos = [
    {
        'author': 'Daniel',
        'description': 'My first todo item!',
        'percentage': '44',
        'deadline': 'February 28, 2022'
    },
    {
        'author': 'Burak',
        'description': 'My Second todo item!',
        'percentage': '77',
        'deadline': 'July 15, 2022'
    },
    {
        'author': 'Max',
        'description': 'My third todo item!',
        'percentage': '99',
        'deadline': 'December 31, 2022'
    }
]



# My views. still not linked between them
def index(request):
    context = {
        'todos': todos
    }
    return render(request, 'todoList/index.html', context)


def how_to_edit_todo(request):
    return render(request, 'todoList/how_to_edit_todo.html')


def add_todo(request):
    return render(request, 'todoList/add_todo.html')


def impressum(request):
    return render(request, 'todoList/impressum.html')

