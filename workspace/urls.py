from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('princess/', views.princess, name='princess'),
    path('test/', views.test, name='test'),
]