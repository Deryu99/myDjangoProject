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


def delete_todo(request, pk):
    todoItem.objects.get(pk=pk).delete()
    return render(request, 'todoList/index.html', {'todos': getTodos()})


def edit_todo(request, pk):
    if request.method == 'POST':
        td = todoItem.objects.get(pk=pk)
        td.description = request.POST.get('description')
        td.deadline = request.POST.get('deadline')
        td.percent = request.POST.get('percent')
        td.save()
        return render(request, 'todoList/index.html', {'todos': getTodos()})

    return render(request, 'todoList/edit_todo.html', {'todo': todoItem.objects.get(pk=pk)})


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
