from errno import ESTALE
from multiprocessing import context
import re
from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, ProfileLink
from .forms import userRegisterForm,updateProfileForm,addLinksForm





def registerView(request):
    form=userRegisterForm()
    if request.method=='POST':
        form=userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeView')  
    context={'form':form}
    return render(request, 'main/signup.html',context)        

def loginView(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profileView')
    return render(request, 'main/login.html')

@login_required(login_url='loginView')
def profileView(request):
    user=request.user
    human=Profile.objects.filter(user=user).first()
    links=ProfileLink.objects.filter(user=human)
    context={'user':user, 'links':links}
    return render(request, 'main/profile.html',context)

@login_required(login_url='loginView')
def updateProfileView(request):
    form=updateProfileForm
    if request.method=='POST':
        form=updateProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profileView')

    context={'form':form}
    return render(request, 'main/updateProfile.html', context)


@login_required(login_url='loginView')
def addProfileLink(request):
    form=addLinksForm
    user=request.user
    print(user)
    if request.method=='POST':
        form=addLinksForm(request.POST, instance=request)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=user
            instance.save()
            return redirect('profileView')
    context={'form':form}
    return render(request, 'main/addProfileLink.html', context)   







def userView(request):
    pass


def homeView(request):
    return render(request, 'main/home.html')




    