from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect, HttpResponse
from proj.app.models.course import Course
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from proj.app.forms import RegistrationForm, LoginForm
from django.views import View
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView

class SignupView(FormView):
    template_name="courses/signup.html"
    form_class=RegistrationForm
    success_url='/login'
    @csrf_exempt
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(FormView):
    template_name="courses/login.html"
    form_class=LoginForm
    success_url='/'
    @csrf_exempt
    def form_valid(self, form):
        login(self.request, form.cleaned_data)
        next_page=self.request.GET.get('next')
        print(self.request.GET)
        if next_page is not None:
            return redirect(next_page)
        print('ln 29 auth.py form is valid ...', form.cleaned_data)
        return super().form_valid(form)

'''
class SignupView(View):

    def get(self, request):
        form=RegistrationForm()
        context={
            'form':form
        }
        return render(request, 'courses/signup.html', context=context)
    
    @csrf_exempt
    def post(self, request):
        print('ln 23 ', request.POST)
        form=RegistrationForm(request.POST)
        #form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            if (user):
                return redirect('login')
        return render(request, 'courses/signup.html', context={'form': form})

'''

'''
def signup(request):
    if request.method=='GET':
        form=RegistrationForm()
        context={
            'form':form
        }
        return render(request, 'courses/signup.html', context=context)

    elif request.method=='POST':
        print('ln 23 ', request.POST)
        form=RegistrationForm(request.POST)
        #form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            if (user):
                return redirect('login')
        return render(request, 'courses/signup.html', context={'form': form})
'''

'''
class LoginView(View):  
    def get(self, request):
        form=LoginForm()        
        context={
            'form':form
        }
        return render(request, 'courses/login.html', context=context)
    
    @csrf_exempt
    def post(self, request):
        form=LoginForm(request=request, data=request.POST)  
        #form=UserCreationForm(request.POST)
        context={
            'form':form
        }
        if form.is_valid():
            return redirect('home')    
        return render(request, 'courses/login.html', context=context)

'''

def signout(request): 
    logout(request)
    request.session.clear()
    return redirect('signup')
    