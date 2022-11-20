from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError

# Create your models here.    
        
class UserCreationForm(UserCreationForm):
    first_name=forms.CharField(max_length=30, required=True)
    last_name=forms.CharField(max_length=30, required=True)
    email=forms.EmailField(max_length=30, required=True)

    def __str__(self):
        return self.name

    class Meta:
        model=User
        fields=["first_name", "last_name", "username", "email", "password1", "password2"]