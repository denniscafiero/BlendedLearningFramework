from django.contrib import admin
# import the .models Resource data info
from .models import Resource, Comment

# then register the Post data with admin site
admin.site.register(Resource)
admin.site.register(Comment)