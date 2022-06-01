from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

from .helpers import *
# Create your models here.
CATEGORY_CHOICES = (
    ("P", "PROGRAMING"),
    ("PR", "PROJECT"),
    ("GM", "GAME"),
)
SUB_CATEGORY_CHOICES = (
    ("C", "C"),
    ("CPP", "CPP"),
    ("JV", "JAVA"),
    ("PY", "PYTHON"),
    ("FL", "FLUTTER"),
    ("GME", "GAME"),
)


class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)
    

class BlogModel(models.Model):
    banner = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=1000, null=True , blank=True)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    # user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, null=True , blank=True)
    sub_category = models.CharField(choices=SUB_CATEGORY_CHOICES, max_length=3, null=True , blank=True) 
    content = models.TextField(null=True , blank=True)
    created_by = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/programing_sitemap/%s/" % self.slug

class BlogImageModel(models.Model):
	image = models.ImageField(upload_to='blog', default="", null=True , blank=True)


       
