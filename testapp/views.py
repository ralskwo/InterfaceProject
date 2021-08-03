from django.shortcuts import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("<h1>테스트 앱입니다.</h1>")

def ddong_Hi(request) :
    return HttpResponse("<h2>안녕하세요! 팀원 정동규입니다.<h2>")