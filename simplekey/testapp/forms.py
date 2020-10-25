from django import forms
from .models import Buy,LandImage,Agent
from django.contrib.auth.models import User



class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'size': '25','placeholder': 'Enter Username','class':'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size': '25','placeholder': 'Enter First Name','class':'form-control'}))

    password = forms.CharField( widget=forms.PasswordInput(attrs={'size': '25','placeholder': 'Enter Password','class':'form-control'}))

    email = forms.CharField( max_length=30, widget=forms.TextInput(attrs={'size': '25','placeholder': 'Enter Email','class':'form-control'}))

    class Meta:
        model=User
        fields=['username','first_name','email','password']


from django.contrib.auth.forms import AuthenticationForm

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'size': '25','placeholder': 'Enter Username','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'size': '25','placeholder': 'Enter Password','class':'form-control'}))



class AgentForm(forms.ModelForm):
    class Meta:
        model=Agent
        fields='__all__'











