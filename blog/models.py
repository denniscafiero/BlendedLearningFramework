from django.db import models
#import the time zone info for date and time
from django.utils import timezone
#import the user
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # on_delete CASCADE means to delete the post if user deleted

