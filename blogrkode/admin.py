from django.contrib import admin

# Register your models here.
from .models import BlogModel,Profile,BlogImageModel
# Register your models here.
admin.site.register(Profile)
admin.site.register(BlogModel)
admin.site.register(BlogImageModel)