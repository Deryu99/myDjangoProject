from django import forms
from .models import todoItem
from django.forms import ModelForm


class AddForm(ModelForm):
    todo = forms.CharField()

    class Meta:
        model = todoItem
        fields = ["description", "deadline", "percent"]
