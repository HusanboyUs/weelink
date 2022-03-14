from dataclasses import field, fields
from operator import mod
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,ProfileLink

class userRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class updateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=('user',)

class addLinksForm(forms.ModelForm):
    class Meta:
        model=ProfileLink
        fields='__all__'


class editProfileLinkForm(forms.ModelForm):
    class Meta:
        model=ProfileLink
        fields='__all__'        