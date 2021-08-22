from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    description = models.TextField(blank=True, max_length=800, name="text")
    complete = forms.BooleanField(required=False)

    class Meta:
        model = Task
        fields = '__all__'
