from rest_framework import serializers 
from base.models import Blog, User


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = User
        fields = ('username' ,'email', 'comment','post')


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Blog
        fields = ('title','content','author','slug','state','category', 'comments')

