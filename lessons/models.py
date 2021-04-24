from django.db import models
#import the time zone info for date and time
from django.utils import timezone
#import the user
from django.contrib.auth.models import User
from django.urls import reverse

SUBJECT = (
    ('Math','Math'),
    ('Science', 'Science'),
    ('Social_Studies','Social Studies'),
    ('English','English'),
    ('Other','Other'),
)
NUMBER_OF_DAYS= (
    ('1','1'),
    ('2', '2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
)
GRADE_LEVEL= (
    ('K-6','K-6'),
    ('7-8', '7-8'),
    ('8-12','8-12'),
)
LOCATION= (
    ('Online','Online'),
    ('In-Person', 'In-Person'),
)

# Create your models here.
class Lessons(models.Model):
    days_in_lesson = models.CharField(max_length=1, choices=NUMBER_OF_DAYS, default='3')
    grade_level = models.CharField(max_length=30, choices=GRADE_LEVEL, default='K-6')
    subject = models.CharField(max_length=30, choices=SUBJECT, default='Math')
    lesson_title = models.CharField(max_length=100)
    lesson_content = models.TextField()
    lesson_goals = models.TextField()
    lesson_class_introduction = models.TextField()

    location_day_one = models.CharField(max_length=30, choices=LOCATION, blank=True)
    lesson_day_one_description = models.TextField(blank=True)
    day_one_url_1 = models.CharField(max_length=256, blank=True) #url for the site
    day_one_url_2 = models.CharField(max_length=256, blank=True) #url for the site
    day_one_url_3 = models.CharField(max_length=256, blank=True) #url for the site
    day_one_url_4 = models.CharField(max_length=256, blank=True) #url for the site

    location_day_two = models.CharField(max_length=30, choices=LOCATION, blank=True)
    lesson_day_two_description = models.TextField(blank=True)
    day_two_url_1 = models.CharField(max_length=256, blank=True)  # url for the site
    day_two_url_2 = models.CharField(max_length=256, blank=True)  # url for the site
    day_two_url_3 = models.CharField(max_length=256, blank=True)  # url for the site
    day_two_url_4 = models.CharField(max_length=256, blank=True)  # url for the site

    location_day_three = models.CharField(max_length=30, choices=LOCATION, blank=True)
    lesson_day_three_description = models.TextField(blank=True)
    day_three_url_1 = models.CharField(max_length=256, blank=True)  # url for the site
    day_three_url_2 = models.CharField(max_length=256, blank=True)  # url for the site
    day_three_url_3 = models.CharField(max_length=256, blank=True)  # url for the site
    day_three_url_4 = models.CharField(max_length=256, blank=True)  # url for the site

    location_day_four = models.CharField(max_length=30, choices=LOCATION, blank=True)
    lesson_day_four_description = models.TextField(blank=True)
    day_four_url_1 = models.CharField(max_length=256, blank=True)  # url for the site
    day_four_url_2 = models.CharField(max_length=256, blank=True)  # url for the site
    day_four_url_3 = models.CharField(max_length=256, blank=True)  # url for the site
    day_four_url_4 = models.CharField(max_length=256, blank=True)  # url for the site

    location_day_five = models.CharField(max_length=30, choices=LOCATION, blank=True)
    lesson_day_five_description = models.TextField(blank=True)
    day_five_url_1 = models.CharField(max_length=256, blank=True)  # url for the site
    day_five_url_2 = models.CharField(max_length=256, blank=True)  # url for the site
    day_five_url_3 = models.CharField(max_length=256, blank=True)  # url for the site
    day_five_url_4 = models.CharField(max_length=256, blank=True)  # url for the site

    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # on_delete CASCADE means to delete the post if user deleted

    def __str__(self):
        return self.lesson_title

    def get_absolute_url(self):
        return reverse('lessons-post-detail', kwargs={'pk': self.pk})