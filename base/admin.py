from django.contrib import admin
from .models import BlogModel, PublishState
# Register your models here.
admin.site.register(BlogModel)
admin.site.register(PublishState)