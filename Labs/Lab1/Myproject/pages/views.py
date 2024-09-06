from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    X={'name':'hashed abdulasalam abdu ali alsubaliti',
       'age':'23', 'names': '', 'size':1}
    return render(request, 'pages/index.html', X)
def index2(request):
    return render(request, 'pages/index2.html')

def index_include(request):
    return render(request, 'pages/index_include.html')

def R(request):
    return HttpResponse('<h2>Anas</h2>')