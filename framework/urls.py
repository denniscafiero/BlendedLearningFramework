from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='framework-home'),
    path('guidelines/course-design/', views.coursedesign, name='framework-course-design'),
    path('guidelines/assessment/', views.assessment, name='framework-assessment'),
    path('guidelines/activities/', views.activities, name='framework-activities'),
    path('guidelines/technology/', views.technology, name='framework-technology'),
    path('guidelines/professional/', views.professional, name='framework-professional')
]
