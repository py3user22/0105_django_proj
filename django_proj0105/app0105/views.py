from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


def home(request):
    return render(request, 'homepage0105.html', {})

def mysql(request):
    return render(request, '0105_mysql_demo3.html', {})

@api_view(['GET', 'POST'])
def books(request):
    return Response('my response is @010524 @1640 jg was here', status=status.HTTP_200_OK)


