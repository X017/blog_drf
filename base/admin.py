from django.contrib import admin
from .models import BlogModel, PublishState, Category, UserComment
# Register your models here.

admin.site.register(BlogModel)
admin.site.register(PublishState)
admin.site.register(Category)
admin.site.register(UserComment)