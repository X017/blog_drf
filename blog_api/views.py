from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from base.models import User, Blog
from .serializer import BlogSerializer, CommentSerializer

class Blog_View(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    
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


class User_View(generics.GenericAPIView):
    queryset = User
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request):
        comments = User.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
