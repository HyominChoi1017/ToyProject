from rest_framework import serializers 
from .models import (Post, User, Comment)
from rest_framework import serializers
from .models import MyUser,PlaylistModle

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'name', 'date_joined']


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistModle
        fields = '__all__'