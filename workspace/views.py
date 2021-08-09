from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import DBCountry, DBPrincess
from os import listdir

def home(request) :
    lat = [51.11318, 57.07817, -17.66184, 39.67106, 51.11318, 46.50811, 46.50811, 17.74521, 61.90783, 61.90783, 46.50811, 23.81171, 29.95436, 37.22095];
    lng = [10.35945, -4.33844, -149.42595, 106.88659, 10.35945, 1.88469, 1.88469, -64.77499, 9.28676, 9.28676, 1.88469, 54.09576, -90.07869, -76.74513];
    hname = ['Rapunzel', 'Merida', 'Moana', 'Mulan', 'SnowWhite', 'Belle', 'Cinderella', 'Ariel', 'Anna', 'Elsa', 'Aurora', 'Jasmine', 'Tiana', 'Pocahontas'];

    # 메인 페이지
    full_name = [i for i in listdir("workspace/static/assets/img/Main1/")]
    princess_name = [name[:name.index('.')] for name in full_name]

    # 지도


    print(lat, latitude)


    full_names = [j for j in listdir("workspace/static/assets/img/Main2/")]
    print(full_names)
    princess_names = enumerate([names[:names.index('.')] for names in full_names], start=1)

    context = {
        'lat': lat, 'lng': lng, 'hname': hname, 'princess_name': princess_name, 'princess_names': princess_names,
    }

    return render(request, "home.html", context)


def princess(request) :
    princess_id = request.GET.get('princess_id')
    context = {'princess_id': princess_id}
    return render(request, "princess.html", context)

def test(request):
    all = DBCountry.objects.all()
    latitude = DBCountry.objects.all().values('latitude')
    longitude = DBCountry.objects.all().values('longitude')