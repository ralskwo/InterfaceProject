from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.
def login(request):
    return render(request, 'account/loginmain.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )
            auth.login(request, user)

            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')