from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect

from .models import User,Playlist
import json
import re
from json.decoder import JSONDecodeError
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.views import View

from django.contrib.auth import login
from django.views.generic.edit import FormView
from .forms import MyUserLoginForm, PlaylistForm, MyUserCreationForm

# Create your views here.

PASSWORD_MINIMUM_LENGTH = 8

class Register(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('main/')
    template_name = 'register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response


class Login(FormView):
    form_class = MyUserLoginForm
    template_name = 'login.jsx'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        return 'main/' # 로그인 성공후 이동할 곳


class UserUpdate(View):
    def post(self, request):
        if request.method == 'POST':
            user = request.user

            email = request.POST.get('email')
            name = request.POST.get('name')
            new_user_pw = request.POST.get('new_user_pw')

            user.username = email
            user.name = name
            user.set_password(new_user_pw)

            user.save()
            return redirect('login.jsx', user.username)
        else:
            return render(request, 'profile.jsx')  # GET 요청에 대한 응답


class PlaySearch(View):
    def search(self, request):
        if request.method == 'POST':
            searched = request.POST['searched']
            playlist = Playlist.objects.filter(name__contains=searched)
            return render(request, 'player.jsx', {'searched': searched, 'playlist': playlist})
        else:
            return render(request, 'player.jsx', {})

class PlayCreate(View):
    def new(self,request):
        form = PlaylistForm()  # 폼 생성
        return render(request, 'player.jsx', {'form': form})
    def create(self,request):
        form = PlaylistForm(request.POST, request.FILES)
        if form.is_valid():
            new_playlist = form.save(commit=False)
            new_playlist.save()
            return redirect('main.html', new_playlist.id)

        return redirect('home')

class PlayRead(View):
    def musicList(self,request):
        musics = Playlist.objects.filter(writer='musician')

        return render(request, 'player.html', {'musics': musics})

    def detail(self,request, Playlist_id):
        details = Playlist.objects.get(pk=Playlist_id)  # 1) pk=Playlist_id를 만족하는 객체 하나
        return render(request, 'main.html', {'details': details})

    # 'user_id','Title','Data','musician','listenDay','listenCount'
class PlayUpdate(View):
    def update(self, request, id):
        update_Playlist = Playlist.objects.get(id=id)

        if request.method == 'POST':
            update_Playlist.user_id = self.request.POST['user_id']
            update_Playlist.Title = self.request.POST['Title']
            update_Playlist.Data = self.request.POST['Date']
            update_Playlist.musician = self.request.POST['musician']
            update_Playlist.listenCount += 1
            update_Playlist.save()
            return redirect('detail', update_Playlist.id)
        elif request.method == 'GET':
            # GET 요청에 대한 처리
            return render(request, 'main.jsx', {'playlist': update_Playlist})
        else:
            return HttpResponseNotAllowed(['GET', 'POST'])

class PlayDelete(View):
    def delete(self, request, id):
        delete_Playlist = Playlist.objects.get(id=id)
        delete_Playlist.delete()
        return redirect('blogList')