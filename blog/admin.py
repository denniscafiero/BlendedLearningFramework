from django.contrib import admin
# import the .models Post data info
from .models import Post
from .models import Resources

# then register the Post data with admin site
admin.site.register(Post)
