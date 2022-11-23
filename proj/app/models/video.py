#import tkinter as tk
#from re import M
from tkinter import *
from tkinter import CASCADE
from django.db import models
from proj.app.models.course import Course

class Video(models.Model):
    title=models.CharField(max_length=30, null=False)
    course=models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    serial_number=models.IntegerField(null=False)
    video_id=models.CharField(max_length=100, null=False)
    is_preview=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
