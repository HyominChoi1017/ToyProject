from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Playlist

from django.contrib.auth import authenticate, login
from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PlaylistModle
from .serializers import PlaylistSerializer

from .models import MyUser
from .serializers import MyUserSerializer


class LoginView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Logged in successfully'})
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        name = request.data.get('name')

        if password1 != password2:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        if MyUser.objects.filter(email=email).exists():
            return Response({'error': 'Email is already in use'}, status=status.HTTP_400_BAD_REQUEST)

        user = MyUser.objects.create_user(email=email, password=password1, name=name)
        serializer = MyUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
class UserDetailView(APIView):
    def get_object(self, pk):
        try:
            return MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = MyUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = MyUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PlaylistList(APIView):
    def get(self, request):
        playlists = PlaylistModle.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaylistDetail(APIView):
    def get_object(self, pk):
        try:
            return PlaylistModle.objects.get(pk=pk)
        except PlaylistModle.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        playlist = self.get_object(pk)
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)

    def put(self, request, pk):
        playlist = self.get_object(pk)
        serializer = PlaylistSerializer(playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        playlist = self.get_object(pk)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

