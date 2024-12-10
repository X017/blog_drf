from django.urls import path
from . import views 
from .views import Blog_View , User_View

urlpatterns = [
    path('blogs/',Blog_View.as_view(),name='blog-list'),
    path('comments/',User_View.as_view(),name='blog-comments')
]