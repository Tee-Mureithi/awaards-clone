from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="Hi I'm new here")
    project = models.ForeignKey(Project,on_delete=models.DO_NOTHING,null=True,blank=True)
    profile_photo = CloudinaryField('images',blank=True,null=True)
    gender = models.CharField(max_length=20)
    contact = models.CharField(max_length = 10,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def projects_posts(self):
        return self.project_set.all()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('profile',args=(str(self.id)))

    @classmethod
    def search_by_user(cls,search_term):
        return cls.objects.filter(user__username__icontains = search_term)

    @classmethod
    def update_profile(cls, id,bio):
        return cls.objects.filter(id = id).update(bio=bio)


DESIGN_CHOICES = [
    (1, '1 '),
    (2, '2 - Horrible'),
    (3, '3 - Terrible'),
    (4, '4 - Bad'),
    (5, '5 - Ok'),
    (6, '6 - Watchable'),
    (7, '7 - Good'),
    (8, '8 - Very Good'),
    (9, '9 - Perfect'),
    (10, '10 - Master Piece')
    
]

USABILITY_CHOICES = [
    (1, '1 - Trash'),
    (2, '2 - Horrible'),
    (3, '3 - Terrible'),
    (4, '4 - Bad'),
    (5, '5 - Ok'),
    (6, '6 - Watchable'),
    (7, '7 - Good'),
    (8, '8 - Very Good'),
    (9, '9 - Perfect'),
    (10, '10 - Master Piece')
    
]

CONTENT_CHOICES = [
    (1, '1 - Trash'),
    (2, '2 - Horrible'),
    (3, '3 - Terrible'),
    (4, '4 - Bad'),
    (5, '5 - Ok'),
    (6, '6 - Watchable'),
    (7, '7 - Good'),
    (8, '8 - Very Good'),
    (9, '9 - Perfect'),
    (10, '10 - Master Piece')
    
]

