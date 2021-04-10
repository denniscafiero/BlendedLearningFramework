from django.urls import path

from .views import (
    CourseDesignResourcesListView,
    AssessmentResourcesListView,
    ActivitiesResourcesListView,
    TechnologyResourcesListView,
    ProfessionalDevelopentResourcesListView,
    ResourceListView,
    ResourceDetailView,
    ResourceCreateView,
)

from . import views #. is current directory and we are bringing in the veiw info

urlpatterns = [
    path('', ResourceListView.as_view(), name='resource-home'),
    path('course-design', CourseDesignResourcesListView.as_view(), name='resource-course-design'),
    path('assessment', AssessmentResourcesListView.as_view(), name='resource-assessment'),
    path('activities', ActivitiesResourcesListView.as_view(), name='resource-activities'),
    path('technology', TechnologyResourcesListView.as_view(), name='resource-technology'),
    path('professional-development', ProfessionalDevelopentResourcesListView.as_view(), name='resource-professional-development'),
    path('post/<int:pk>/', ResourceDetailView.as_view(), name='resource-post-detail'),
    path('post/new/', ResourceCreateView.as_view(), name='resource-post-create'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
