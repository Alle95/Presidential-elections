import getpass
import os
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import textForm

def home_page(request):
    if request.user.is_authenticated:
        descriptions = text.objects.all()
        return render(request,'home.html', {"descriptions": descriptions})
    else:
        return render(request,'home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Registration Successful!"))
            return redirect('homePage', {'form':request.user.username})
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            messages.success(request,("There was an error, Please try again..."))
            return redirect('login')
    else:    
        return render(request, 'login.html', {})
    
def logout_user(request):
    logout(request)
    return redirect('homePage')

def profile_user(request, user_id):
    description = text.objects.filter(user_id=user_id)
    form = textForm(request.POST or None)
    if request.method == 'POST':
        if description.exists():
            return render(request, 'profile.html', {'form':form, 'description':description})
        else :
            if form.is_valid():
                object = form.save(commit=False)
                object.user = request.user
                object.save()
                return redirect('profile', user_id)
    return render(request, 'profile.html', {'form':form, 'description':description})


def delete_desc(request, user_id):
    description = text.objects.filter(user_id=user_id)
    description.delete()
    return redirect('profile', user_id)

def edit_desc(request, user_id):
    description = text.objects.get(user_id=user_id)
    form = textForm(instance=description)
    if request.method == 'POST':
        form = textForm(request.POST, instance=description)
        if form.is_valid():
            description = form.save(commit=False)
            description.user = request.user
            description.save()
            return redirect('profile', user_id)
    else:    
        return render(request, 'edit_desc.html', {'form':form, 'description':description})
    
def apply_presid(request, user_id):
    