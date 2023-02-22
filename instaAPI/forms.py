from .models import Playlist, User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['user_id', 'Title', 'Data', 'musician', 'listenDay', 'listenCount']


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class MyUserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Invalid login credentials')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('Inactive user')
        return cleaned_data

    def get_user(self):
        return self.user_cache