from django.shortcuts import render, redirect
from django.http import HttpResponse
from todoList.models import todoItem
from django.contrib import messages
from django import forms

# Fetch all todoItem(s) from database
data = todoItem.objects.all()


# My views.
def index(request):
    return render(request, 'todoList/index.html', {'todos': data})


# insert todoItem to the db, has an error that I cant find or maybe inserted the data but cant see
def insert_todo(request):
    form = add_todo(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "To-DO saved successfully!")
    context = {'form': form}
    return render(request, 'todoList/add_todo.html', context)


# Methods in index

# it deletes a todoItem from the db but it is not shown on the webpage ...
def delete_todoItem(request, pk):
    if request.method == "POST":
        td = todoItem.objects.get(pk=pk)
        td.delete()
        return redirect('/')

    return render(request, '/', {'todos': data})


def how_to_edit_todo(request):
    return render(request, 'todoList/how_to_edit_todo.html')


def add_todo(request):
    return render(request, 'todoList/add_todo.html')


def impressum(request):
    return render(request, 'todoList/impressum.html')

# dummy todos (not using this anymore, some already in the database)
# todos = [
#     {
#         'description': 'My first todo item!',
#         'percentage': '44',
#         'deadline': 'May 10, 2021, 4:55 a.m.'
#     },
#     {
#         'description': 'My Second todo item!',
#         'percentage': '77',
#         'deadline': 'May 10, 2021, 5:06 a.m.'
#     },
#     {
#         'description': 'My third todo item!',
#         'percentage': '99',
#         'deadline': 'May 10, 2021, 5:07 a.m.'
#     }
# ]
