# api/admin.py

# django imports
from django.contrib import admin

# local imports
from .models import Post, User

admin.site.register(User)
admin.site.register(Post)
