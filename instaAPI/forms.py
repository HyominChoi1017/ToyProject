from .models import Playlist
from django import forms
from django.contrib.auth import get_user_model
from django import forms
from .models import MyUser, PlaylistModle
User = get_user_model()

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['user', 'title', 'data', 'musician', 'listen_day', 'listen_count']




class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email', 'name']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)


class PlaylistModelForm(forms.ModelForm):
    class Meta:
        model = PlaylistModle
        fields = ['name', 'description', 'songs']

