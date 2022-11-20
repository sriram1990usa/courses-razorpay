from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate

class LoginForm(AuthenticationForm):
    #email=forms.EmailField(required=True)
    username= forms.EmailField(max_length=30, required=True, label='Email Address')
    
    def clean(self):
        email=self.cleaned_data['username']
        password=self.cleaned_data['password']
        
        user=None
        try:
            user=User.objects.get(email=email)         
            result=authenticate(username=user.username,
                     password=password)

            if(result is not None):
                print('ln 23 in self.request in login_form.py ', self.request)
                print('ln 22 result in login_form.py ', result)
                return result
            else:
                raise ValidationError("email or pwd incorrect")

        except:
            raise ValidationError("email or pwd invalid")