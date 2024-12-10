from rest_framework import generics
from base.models import User, Blog
from .serializer import BlogSerializer

class Blog_View(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

