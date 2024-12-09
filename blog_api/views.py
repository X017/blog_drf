from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import BlogSerializer
from base.models import BlogModel  
from rest_framework import status





@api_view(['GET'])
def viewData(request):
    Blog = BlogModel.objects.all()
    serializer = BlogSerializer(Blog,many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    username = request.POST
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

