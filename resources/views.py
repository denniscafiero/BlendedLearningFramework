from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Resource
# Create your views here.
def home(request):
    #creating a dictionary for the content of the post
    context = {
        'resources': Resource.objects.all() #takes all the posts in the database
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/home.html', context)

def CourseDesignResources(request):
    #creating a dictionary for the content of the post
    context = {
        'resources': Resource.objects.all(), #takes all the posts in the database
        'filter': 'course_design'
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/filter_resource.html', context)

def AssessmentResources(request):
    #creating a dictionary for the content of the post
    context = {
        'resources': Resource.objects.all(), #takes all the posts in the database
        'filter': 'assessment'
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/filter_resource.html', context)

def ActivitiesResources(request):
    #creating a dictionary for the content of the post
    context = {
        'resources': Resource.objects.all(), #takes all the posts in the database
        'filter': 'activities'
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/filter_resource.html', context)

def ProfessionalDevelopmentResources(request):
    #creating a dictionary for the content of the post
    context = {
        'resources': Resource.objects.all(), #takes all the posts in the database
        'filter': 'professional_development'
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/filter_resource.html', context)

def TechnologyResources(request):
    #creating a dictionary for the content of the post
    context = {
        'resources': Resource.objects.all(), #takes all the posts in the database
        'filter': 'technology'
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/filter_resource.html', context)

#create the detail view for the page
class ResourceDetailView(DetailView):
    model = Resource

# create the create view for the blog post will be a form
class ResourceCreateView(LoginRequiredMixin, CreateView):
    model = Resource
    fields = ['title', 'content', 'framework_category', 'site_url']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)