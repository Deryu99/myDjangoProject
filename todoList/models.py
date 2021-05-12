from django.db import models
from django.forms import ModelForm
from django import forms

# model for todos
class todoItem(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    description = models.TextField(max_length=160)
    deadline = models.DateTimeField() # ...
    percent = models.IntegerField() # Needs to be between 0 and 100!

    def __str__(self):
        return self.description

class addForm(ModelForm):
    class Meta:
        model = todoItem
        fields = ['description', 'deadline', 'percent']