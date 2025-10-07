from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'username', 'content', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at', 'username']


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)  # nested read-only list
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'username', 'title', 'content', 'created_at', 'updated_at', 'comments', 'comment_count']
        read_only_fields = ['user', 'created_at', 'updated_at', 'comments', 'comment_count', 'username']
