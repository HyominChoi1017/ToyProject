from django import forms
from .models import Playlist

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['user_id','Title','Data','musician','listenDay','listenCount']
