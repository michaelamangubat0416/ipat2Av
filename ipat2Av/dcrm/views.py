from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import SignUpForm
# Create your views here.
def home(request):
    data=Record.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          messages.success(request, "You have successfully logged in!")
          return redirect('home')
        else:
          messages.success(request, "There was an error logging in! Please try again.")
          return redirect('home')

    return render(request, 'home.html', {'data':data})

def register(request):
    if request.method=='POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered!")
            return redirect('home')
    else:
        form= SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, "You successfully logged out your account!" )
    return redirect('home')