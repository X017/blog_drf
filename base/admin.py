from django.contrib import admin
from .models import Blog, Category, User, PublishState
# Register your models here.

admin.site.register(PublishState)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Blog)