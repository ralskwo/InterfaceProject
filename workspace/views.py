from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader


def home(request) :
    return render(request, 'home.html')


def princess(request) :
    return render(request, 'princess.html')


# Create your views here.
