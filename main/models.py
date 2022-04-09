from django.db import models
# from django.contrib.auth.decorators import login_required
# Create your models here.
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.Charfield(max_length=50)
    image = CloudinaryField('images')
    description