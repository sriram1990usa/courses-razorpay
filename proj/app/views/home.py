from django.shortcuts import render
from django.shortcuts import HttpResponse
from proj.app.models.course import Course
from django.views.generic import ListView
# Create your views here.
class HomePageView(ListView):
    template_name='courses/home.html'
    #queryset=Course.objects.all()
    queryset=Course.objects.filter(active=True)    
    #context_object_name='courses'
'''
def home(request):    
    courses=Course.objects.all()   
    context={'courses': courses } 
    return render(request, 'courses/home.html', context)#ok ok
    
'''
