from rest_framework import serializers
from .data import getMusicChart
from .models import *
 
class MusicChartSerializer(serializers.Serializer):
    data = serializers.JSONField(default={
        'chart':{}
    })

class ArtistCharSerializer(serializers.Serializer):
    pass