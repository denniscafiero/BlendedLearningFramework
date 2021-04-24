from django.urls import path

from .views import (
    LessonCreateView,
    LessonDetailView,

)

from . import views #. is current directory and we are bringing in the veiw info

urlpatterns = [
    path('', views.home, name='lessons-home'),
    path('post/new/', LessonCreateView.as_view(), name='lessons-post-create'),
    path('post/<int:pk>/', LessonDetailView.as_view(), name='lessons-post-detail'),
    path('math', views.MathLessons, name='lessons-math'),
    path('english', views.EnglishLessons, name='lessons-english'),
    path('socialstudies', views.SocialStudiesLessons, name='lessons-social-studies'),
    path('science', views.ScienceLessons, name='lessons-science'),
    path('other', views.OtherLessons, name='lessons-other'),
]