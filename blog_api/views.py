from rest_framework import generics
from rest_framework.response import Response

from base.models import User, Blog
from .serializer import BlogSerializer

class Blog_View(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs,many=True)
        return Response(serializer.data)

