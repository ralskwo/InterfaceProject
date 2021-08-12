from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import *
from os import listdir, walk

def home(request) :
    # 메인 페이지
    full_name_main1 = [i for i in listdir("workspace/static/assets/img/Main1/")]
    princess_name1 = [name[:name.index('.')] for name in full_name_main1]
    full_name_main2 = [i for i in listdir("workspace/static/assets/img/Main1/")]
    princess_name2 = [name[:name.index('.')] for name in full_name_main2]

    # 지도
    princess_list = DBPrincess.objects.all()
    princess_list = [["/static/assets/img/Markers/" + p.name + ".png",
                      float(p.country.latitude),
                      float(p.country.longitude),
                      p.name,
                      str(p.age),
                      p.country.country] for p in princess_list]

    context = {
        'princess_name1': princess_name1, 'princess_name2': princess_name2, 'princess_list': princess_list,
    }

    return render(request, "home.html", context)


def princess(request) :
    princess_name = request.GET.get('princess_name')
    img_list = []

    root_img_folder = "workspace/static/assets/img"
    for rt, _, files in walk(root_img_folder):
        folder_name = rt[rt.index('img') + 4:].lower()
        if folder_name == princess_name.lower():
            img_list = files
            break

    full_name_main1 = [i for i in listdir("workspace/static/assets/img/Main1/")]
    princess_name1 = [name[:name.index('.')] for name in full_name_main1]

    princess_info = DBInfomation.objects.all()
    info_list = [[info.princess.name,
                  str(info.princess.age),
                  info.princess.country.country,
                  info.info,
                  info.personality,
                  info.characteristic] for info in princess_info]

    specific_info = []
    for i in range(len(info_list)):
        if info_list[i][0] == princess_name:
            specific_info = info_list[i]
            break


    quoats_all = [[q.princess.name,
                    q.quoat_eng,
                    q.quoat_kor] for q in DBQuoats.objects.all()]

    quoats_list = []
    for name, eng, kor in quoats_all:
        if name.lower() == princess_name.lower():
            quoats_list.append([eng, kor])


    context = {
        'princess_name1': princess_name1,
        'img_list': list(enumerate(img_list, start=1)),
        'folder_name': folder_name,
        'info_list': info_list,
        'specific_info': specific_info,
        'quoats_list': list(enumerate(quoats_list)),
    }

    return render(request, "princess.html", context)


def test(request):
    princess_list = DBPrincess.objects.all()
    princess_dict = dict()

    full_name = [i for i in listdir("workspace/static/assets/img/Main1/")]
    princess_name = [name[:name.index('.')] for name in full_name]

    for p in princess_list:
        princess_dict[p.name] = {'lat': float(p.country.latitude), 'lng': float(p.country.longitude)}
        print(p.name, princess_dict[p.name])

    context = {"princess_dict": princess_dict, "princess_name": princess_name}

    return render(request, "test.html", context)