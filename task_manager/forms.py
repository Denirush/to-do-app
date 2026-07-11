from django import forms
from .models import TaskList
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields= ['name','completed']