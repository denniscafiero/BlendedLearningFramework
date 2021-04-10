from django.contrib import admin
# import the .models Post data info
from .models import Post, Comment
from .models import Resources

# then register the Post data with admin site
admin.site.register(Post)
admin.site.register(Comment)
