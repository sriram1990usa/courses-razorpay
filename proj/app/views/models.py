from django.contrib.auth.models import Group, User
from rest_framework import serializers
from django.db.models import models

class User(models.Model):
    class Meta:
        model=User
        fields=['url','username','email','groups']

class GroupSerializer(models.Model):
    class Meta:
        model=Group
        fields=['url','name']
        
