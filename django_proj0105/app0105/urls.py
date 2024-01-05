from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('homepage', views.home),
    path('homepage0105.html', views.home),
]