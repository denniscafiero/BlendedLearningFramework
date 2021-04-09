from django.urls import path

from .views import (
    ResourceDetailView,
    ResourceCreateView,
)

from . import views #. is current directory and we are bringing in the veiw info

urlpatterns = [
    path('', views.home, name='resource-home'),
    path('course-design', views.CourseDesignResources, name='resource-course-design'),
    path('assessment', views.AssessmentResources, name='resource-assessment'),
    path('activities', views.ActivitiesResources, name='resource-activities'),
    path('technology', views.TechnologyResources, name='resource-technology'),
    path('professional-development', views.ProfessionalDevelopmentResources, name='resource-professional-development'),
    path('post/<int:pk>/', ResourceDetailView.as_view(), name='resource-post-detail'),
    path('post/new/', ResourceCreateView.as_view(), name='resource-post-create'),
]
