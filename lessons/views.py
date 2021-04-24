from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
from .models import Lessons

# Create your views here.
def home(request):

    #resource_info = Resource.objects.filter(framework_category='course_design')
    lessons_info = Lessons.objects.all()
    #creating a dictionary for the content of the post
    context = {
        'lessons': lessons_info #takes all the posts in the database
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'lessons/home.html', context)

# create the create view for the lesson will be a form
class LessonCreateView(LoginRequiredMixin, CreateView):
    model = Lessons
    fields = ['days_in_lesson', 'grade_level', 'subject', 'lesson_title', 'lesson_content', 'lesson_goals', 'lesson_class_introduction',
              'location_day_one', 'lesson_day_one_description', 'day_one_url_1', 'day_one_url_2', 'day_one_url_3', 'day_one_url_4',
              'location_day_two', 'lesson_day_two_description', 'day_two_url_1', 'day_two_url_2', 'day_two_url_3',
              'day_two_url_4',
              'location_day_three', 'lesson_day_three_description', 'day_three_url_1', 'day_three_url_2', 'day_three_url_3',
              'day_three_url_4',
              'location_day_four', 'lesson_day_four_description', 'day_four_url_1', 'day_four_url_2', 'day_four_url_3',
              'day_four_url_4',
              'location_day_five', 'lesson_day_five_description', 'day_five_url_1', 'day_five_url_2', 'day_five_url_3',
              'day_five_url_4',
              ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#create the detail view for the page
class LessonDetailView(DetailView):
    model = Lessons

def MathLessons(request):
    lessons_info = Lessons.objects.filter(subject='Math')

    #creating a dictionary for the content of the post
    context = {
        'lessons': lessons_info, #takes all the posts in the database
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'lessons/home.html', context)

def ScienceLessons(request):
    lessons_info = Lessons.objects.filter(subject='Science')

    #creating a dictionary for the content of the post
    context = {
        'lessons': lessons_info, #takes all the posts in the database
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'lessons/home.html', context)

def SocialStudiesLessons(request):
    lessons_info = Lessons.objects.filter(subject='Social_Studies')

    #creating a dictionary for the content of the post
    context = {
        'lessons': lessons_info, #takes all the posts in the database
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'lessons/home.html', context)

def EnglishLessons(request):
    lessons_info = Lessons.objects.filter(subject='English')

    #creating a dictionary for the content of the post
    context = {
        'lessons': lessons_info, #takes all the posts in the database
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'lessons/home.html', context)

def OtherLessons(request):
    lessons_info = Lessons.objects.filter(subject='Other')

    #creating a dictionary for the content of the post
    context = {
        'lessons': lessons_info, #takes all the posts in the database
    }
    #passing the context to the template will allow us to access it in template
    return render(request, 'lessons/home.html', context)