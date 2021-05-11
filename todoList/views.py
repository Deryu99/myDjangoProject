from django.shortcuts import render, redirect
from django.http import HttpResponse
from todoList.models import todoItem, addForm
from django.contrib import messages
from django import forms

# Fetch all todoItem(s) from database
def getTodos():
    return todoItem.objects.all()

# My views.
def index(request):
    context = {
        'todos': getTodos()
    }
    return render(request, 'todoList/index.html', context)

def delete_or_edit_todo(request, pk):
    # GET -> deletes todo
    if request.method == 'GET':
        todoItem.objects.get(pk=pk).delete()
    # POST -> updates it
    elif request.method == 'POST':
        todoItem.objects.get(pk=pk)

    return render(request, 'todoList/index.html', {'todos': getTodos()})

def how_to_edit_todo(request):
    return render(request, 'todoList/how_to_edit_todo.html')


def add_todo(request):
    if request.method == 'POST':
        form = addForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'To-Do saved successfully!')
        return render(request, 'todoList/add_todo.html', {'form': form})
    
    return render(request, 'todoList/add_todo.html')


def impressum(request):
    return render(request, 'todoList/impressum.html')
