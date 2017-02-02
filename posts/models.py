from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', default='Images/None/No-img.jpg')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)   
    author = models.ForeignKey(User, null=True)


    class Meta:
        ordering =['created','updated']

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    text = models.TextField()
    post = models.ForeignKey(Post,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ['created_on']

    def __unicode__(self):
        return self.name


