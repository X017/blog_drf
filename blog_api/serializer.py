from rest_framework import serializers 
from base.models import BlogModel , UserComment


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = UserComment 
        fields = ('username' ,'email', 'comment','post')


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = BlogModel
        fields = ('title','content','author','slug','state','category', 'comments')

