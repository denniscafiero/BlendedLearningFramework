from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Framework and Site Home Page</h1>')
