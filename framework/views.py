from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'framework/home2.html', {'title': 'Home'})

def coursedesign(request):
    return render(request, 'framework/course-design.html', {'title': 'Course Design Guidelines'})

def assessment(request):
    return render(request, 'framework/assessment.html', {'title': 'Assessment Guidelines'})

def activities(request):
    return render(request, 'framework/activities.html', {'title': 'Guidelines for Activities'})

def technology(request):
    return render(request, 'framework/technology.html', {'title': 'Technology and Tools Guidelines'})

def professional(request):
    return render(request, 'framework/professional-development.html', {'title': 'Professional Development Guidelines'})
