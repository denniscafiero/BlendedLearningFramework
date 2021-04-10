from django.db import models
#import the time zone info for date and time
from django.utils import timezone
#import the user
from django.contrib.auth.models import User
from django.urls import reverse

CATEGORY_CHOICES = (
    ('course_design','Course Design'),
    ('assessment', 'Assessment'),
    ('activities','Activities'),
    ('technology','Technology and Tools'),
    ('professional_development','Professional development'),
)

class Resource(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    site_url = models.CharField(max_length=256) #url for the site
    framework_category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='course_design')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # on_delete CASCADE means to delete the post if user deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resource-post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey('resources.Resource', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text