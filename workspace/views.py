from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import DBCountry, DBPrincess

def home(request) :
    lat = [51.11318, 57.07817, -17.66184, 39.67106, 51.11318, 46.50811, 46.50811, 17.74521, 61.90783, 61.90783, 46.50811, 23.81171, 29.95436, 37.22095];
    lng = [10.35945, -4.33844, -149.42595, 106.88659, 10.35945, 1.88469, 1.88469, -64.77499, 9.28676, 9.28676, 1.88469, 54.09576, -90.07869, -76.74513];
    hname = ['Rapunzel', 'Merida', 'Moana', 'Mulan', 'SnowWhite', 'Belle', 'Cinderella', 'Ariel', 'Anna', 'Elsa', 'Aurora', 'Jasmine', 'Tiana', 'Pocahontas'];
    context = {
        'lat': lat, 'lng': lng, 'hname': hname
    }
    return render(request, "home.html", context)


def princess(request) :
    return render(request, "princess.html")

def Mainimg(request):
    context = {'alph': [chr(i) for i in range((ord('A'),ord('T')+1))]}
    return render(request, 'home.html', context)

def individual_character(request):
    princess_id = request.GET.get('princess_id')
    context = {'princess_id': princess_id}
    return render(request, 'princess.html', context)

