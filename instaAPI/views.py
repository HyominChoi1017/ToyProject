from django.shortcuts import render, redirect
from .models import User,Playlist
import json
import re
from json.decoder import JSONDecodeError

from django.http import JsonResponse
from django.views import View
from django.db.models import Q

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
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


class UserUpdate(View):
    def update(self,request):
        if request.method == 'GET':
            return render(request, 'profile.jsx')  # 프로필위치

        elif request.method == 'POST':
            user = request.user

            email = request.POST.get('email')
            name = request.POST.get('name')
            new_user_pw = request.POST.get('new_user_pw')

            user.Username = email
            user.Name = name
            user.Password(new_user_pw)

            user.save()
            return redirect('login.jsx', user.Username)


class PlaySearch(View):
    def search(self, request):
        if request.method == 'POST':
            searched = request.POST['searched']
            playlist = Playlist.objects.filter(name__contains=searched)
            return render(request, 'main.jsx', {'searched': searched, 'playlist': playlist})
        else:
            return render(request, 'main.jsx', {})
