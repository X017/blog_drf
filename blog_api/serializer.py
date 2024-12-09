from rest_framework import serializers 
from base.models import BlogModel


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ('title','content','author','slug','state')