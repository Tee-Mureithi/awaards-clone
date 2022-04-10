from django.contrib import admin
from .models import Project,Profile,Rate

# Register your models here.

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Rate)