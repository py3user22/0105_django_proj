from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homepage0105.html', {})

def mysql(request):
    return render(request, '0105_mysql_demo3.html', {})


