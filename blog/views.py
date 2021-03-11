from django.shortcuts import render
from django.http import HttpResponse

#lets import the posts .models just means lets use models in this directory
from .models import Post


posts = [
    {
        'author': 'Dennis',
        'title' : 'This is the Title',
        'content': 'This is the content for the blog post',
        'date_posted': 'March, 8th, 2021'
    },
    {
        'author': 'Jane',
        'title' : 'This is the Title 2',
        'content': 'This is the content for the blog post 2',
        'date_posted': 'March, 7th, 2021'
    }
]


def home(request):
    #creating a dictionary for the content of the post
    context = {
        'posts': Post.objects.all() #takes all the posts in the database
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})