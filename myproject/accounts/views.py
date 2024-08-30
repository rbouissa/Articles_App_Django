from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth import authenticate
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "User created successfully!")
            return redirect(reverse('article_list'))
        else :
             messages.success(request, "User created successfully!")
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None : 
                auth_login(request, user)
                return redirect (reverse('article_list'))
            else:
                messages.error(request, "Invalid username or password.")

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('article_list')