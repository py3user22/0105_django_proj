from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('homepage', views.home),
    path('homepage0105.html', views.home),
    path('0105_mysql_demo3.html', views.mysql),
    path('mysql_demo3', views.mysql),
]