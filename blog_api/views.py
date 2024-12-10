from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from base.models import User, Blog
from .serializer import BlogSerializer

class Blog_View(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

class Comment_View(generics):
    pass