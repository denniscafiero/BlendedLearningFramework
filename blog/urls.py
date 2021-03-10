from django.urls import path
from . import views #. is current directory and we are bringing in the veiw info

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
