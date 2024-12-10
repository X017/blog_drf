from django.urls import path
from . import views 
from .views import Blog_View

urlpatterns = [
    path('blogs/',Blog_View.as_view(),name='blog-list')
]