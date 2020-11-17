from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h1>Windows Cleaning Homepage</h1>")
    return render(request, 'base.html')
