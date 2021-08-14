from os import listdir
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth

# Create your views here.
def login(request):
    # Side bar 페이지 이동 링크
    full_name_main1 = [i for i in listdir("workspace/static/assets/img/Main1/")]
    princess_name1 = [name[:name.index('.')] for name in full_name_main1]
    context = {'princess_name1': princess_name1}
    return render(request, 'account/loginmain.html', context)

def signup(request):
    full_name_main1 = [i for i in listdir("workspace/static/assets/img/Main1/")]
    princess_name1 = [name[:name.index('.')] for name in full_name_main1]
    context = {'princess_name1': princess_name1}

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )
            auth.login(request, user)

            return redirect('/')
        return render(request, 'signup.html', context)
    return render(request, 'signup.html', context)