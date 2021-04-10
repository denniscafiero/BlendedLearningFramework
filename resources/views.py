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

    #resource_info = Resource.objects.filter(framework_category='course_design')
    resource_info = Resource.objects.all()
    #creating a dictionary for the content of the post
    context = {
        'resources': resource_info #takes all the posts in the database
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/home.html', context)

class ResourceListView(ListView):
    model = Resource
    template_name = 'resources/home.html'
    context_object_name = 'resources'
    ordering = ['-date_posted']
    paginate_by = 2

class CourseDesignResourcesListView(ListView):
    #resource_info = Resource.objects.filter(framework_category='course_design')
    #creating a dictionary for the content of the post
    #model = Resource.objects.filter(framework_category='course_design')
    template_name = 'resources/home.html'
    context_object_name = 'resources'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        return Resource.objects.filter(framework_category='course_design')

def CourseDesignResources(request):
    resource_info = Resource.objects.filter(framework_category='course_design')
    #creating a dictionary for the content of the post
    context = {
        'resources': resource_info, #takes all the posts in the database
        'filter': 'course_design'
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/filter_resource.html', context)

class AssessmentResourcesListView(ListView):
    #resource_info = Resource.objects.filter(framework_category='course_design')
    #creating a dictionary for the content of the post
    #model = Resource.objects.filter(framework_category='course_design')
    template_name = 'resources/home.html'
    context_object_name = 'resources'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        return Resource.objects.filter(framework_category='assessment')

def AssessmentResources(request):
    resource_info = Resource.objects.filter(framework_category='assessment')
    #creating a dictionary for the content of the post
    context = {
        'resources': resource_info, #takes all the posts in the database
        'filter': 'assessment'
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/filter_resource.html', context)

class ActivitiesResourcesListView(ListView):
    #resource_info = Resource.objects.filter(framework_category='course_design')
    #creating a dictionary for the content of the post
    #model = Resource.objects.filter(framework_category='course_design')
    template_name = 'resources/home.html'
    context_object_name = 'resources'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        return Resource.objects.filter(framework_category='activities')

def ActivitiesResources(request):
    resource_info = Resource.objects.filter(framework_category='activities')

    #creating a dictionary for the content of the post
    context = {
        'resources': resource_info, #takes all the posts in the database
        'filter': 'activities'
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/filter_resource.html', context)

class ProfessionalDevelopentResourcesListView(ListView):
    #resource_info = Resource.objects.filter(framework_category='course_design')
    #creating a dictionary for the content of the post
    #model = Resource.objects.filter(framework_category='course_design')
    template_name = 'resources/home.html'
    context_object_name = 'resources'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        return Resource.objects.filter(framework_category='professional_development')

def ProfessionalDevelopmentResources(request):
    resource_info = Resource.objects.filter(framework_category='professional_development')

    #creating a dictionary for the content of the post
    context = {
        'resources': resource_info, #takes all the posts in the database
        'filter': 'professional_development'
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'resources/filter_resource.html', context)

class TechnologyResourcesListView(ListView):
    #resource_info = Resource.objects.filter(framework_category='course_design')
    #creating a dictionary for the content of the post
    #model = Resource.objects.filter(framework_category='course_design')
    template_name = 'resources/home.html'
    context_object_name = 'resources'
    ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        return Resource.objects.filter(framework_category='technology')

def TechnologyResources(request):
    resource_info = Resource.objects.filter(framework_category='technology')
    #creating a dictionary for the content of the post
    context = {
        'resources': resource_info, #takes all the posts in the database
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