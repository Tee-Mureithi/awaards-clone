from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# Create your models here.
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.Charfield(max_length=50)
    image = CloudinaryField('images')
    description = models.TextField()
    link = models.URLField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def get_absolute_url(self):
        return reverse('home')

    @classmethod
    def search_by_title(cls,search_term):
        return cls.objects.filter(title__icontains = search_term)

    @classmethod
    def update_project(cls, id,title):
        return cls.objects.filter(id = id).update(title=title)


    class Meta:
        ordering = ['-created_at']