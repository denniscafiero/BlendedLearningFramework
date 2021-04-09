from django.shortcuts import render
from django.http import HttpResponse
from .models import Resource
# Create your views here.
def home(request):
    #creating a dictionary for the content of the post
    context = {
        'resources': Resource.objects.all() #takes all the posts in the database
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/home.html', context)