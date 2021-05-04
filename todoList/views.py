from django.shortcuts import render
from django.http import HttpResponse

# My views. still not linked between them
def index(request):
    return render(request, 'todoList/index.html')


def how_to_edit_todo(request):
    return render(request, 'todoList/how_to_edit_todo.html')


def add_todo(request):
    return render(request, 'todoList/add_todo.html')


def impressum(request):
    return render(request, 'todoList/impressum.html')

