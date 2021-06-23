from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
##registr form
class Registerform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Create password...'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm password..'}))
    class Meta:
        model=User
        fields=['username','first_name','email']
        labels = {'first_name': 'Enter Your Name',
                  'email': 'Email Address'}

        widgets = {'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter username...'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your Name'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Valid email address'})}

class Logonform(AuthenticationForm):

    username =forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,'class': 'form-control','placeholder':'Enter username.....'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter password...'}))
    class Meta:
        model = User
        fields = ['username']