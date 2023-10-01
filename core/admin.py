from django.contrib import admin
from .models import Post, ProjectField, Project

# Register your models here.
admin.site.register(Post)
admin.site.register(ProjectField)
admin.site.register(Project)