from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import BlogSerializer
from base.models import BlogModel, PublishState, Category  
from rest_framework import status




@api_view(['GET'])
def viewData(request):
    state = request.GET.get('state')
    if state:
        try:
            state = int(state)
            if state in [PublishState.State.DRAFT, PublishState.State.PUBLISHED, PublishState.State.ARCHIVED]:
                blogs = BlogModel.objects.filter(state__state=state)
            else:
                return Response({'error': 'Invalid state.'}, status=400)
        except ValueError:
            return Response({'error': 'State must be an integer.'}, status=400)
    else:
        blogs = BlogModel.objects.all()
    
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    username = request.POST
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

