from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import (User, Post, Comment)
from .serializers import (PostSerializer, UserSerializer, CommentSerializer)

import json
import re
from json.decoder import JSONDecodeError
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.

PASSWORD_MINIMUM_LENGTH = 8

class Register(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            Username = data.get('Username', None)
            Name = data.get('Name', None)
            password = data.get('password', None)

            Username_pattern = re.compile('[^@]+@[^@]+\.[^@]+') #골뱅이 포함 구분하기 위함
            Name_pattern = re.compile('^(?=.*[a-z])[a-z0-9_.]+$') #이름 . _ 포함 하지않도록

            if not (
                    Username
                    and Name
                    and password
            ):
                return JsonResponse({'message': 'KEY_ERROR'}, status=400)

            if Username:
                if not re.match(Username_pattern, Username):
                    return JsonResponse({'message': 'EMAIL_VALIDATION_ERROR'}, status=400)

            if not re.match(Name_pattern, Name):
                return JsonResponse({'message': 'USERNAME_VALIDATION_ERROR'}, status=400)

            if len(data['password']) < PASSWORD_MINIMUM_LENGTH:
                return JsonResponse({'message': 'PASSWORD_VALIDATION_ERROR'}, status=400)

            if User.objects.filter(
                    Q(email=data.get('email', 1)) |
                    Q(mobile_number=data.get('mobile_number', 1)) |
                    Q(username=data['username'])
            ).exists():
                return JsonResponse({'message': 'ALREADY_EXISTS'}, status=409)

            User.objects.create(
                Name=Name,
                Username=Username,
                password=password
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)

class Login(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            login_id = data.get('id', None)
            password = data.get('password', None)

            if not (login_id and password):
                return JsonResponse({'message': 'KEY_ERROR'}, status=400)

            if not User.objects.filter(
                    Q(Username=login_id)
            ).exists():
                return JsonResponse({'message': 'INVALID_USER'}, status=401)

            user = User.objects.get(
                    Q(Username=login_id)
            )

            if user.password != password:
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)

            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)


class PostView(APIView):
    def get(self, request): 
        query = Post.objects.all() 
        serializer = PostSerializer(query, many=True)
        print("data:", serializer.data)
        return Response(serializer.data)

    def post(self, request):
            serializer = PostSerializer(data = request.data, many=True)
            # 나중에 유효성검사 진행하셈
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SinglePostView(APIView):
    def get(self, request, post_id):
        query = Post.objects.filter(id=post_id)
        print("data:", query)
        serializer = PostSerializer(query, many=False)
        return Response(serializer.data)

class UserView(APIView):
    def get(self, request, user_id):
        query = User.objects.filter(id=user_id)
        serializer = UserSerializer(query, many=False)
        return Response(serializer.data)

class CommentView(APIView):
    def get(self, request, post_id):
        query = Comment.objects.filter(post_id=post_id)
        serializer = CommentSerializer(query, many=True)
        print("Comments of PostID {}: {}".format(post_id, serializer.data))
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data = request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
