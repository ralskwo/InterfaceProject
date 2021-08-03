from django.shortcuts import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("<h1>테스트 앱입니다.</h1>")