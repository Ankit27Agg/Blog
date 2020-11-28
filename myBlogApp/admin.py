from django.contrib import admin
from .models import Post, Postcomment

# Register your models here.
admin.site.register((Post, Postcomment))