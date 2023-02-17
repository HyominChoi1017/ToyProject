from rest_framework import serializers
from .data import getMusicChart
from .models import *
 
class MusicChartSerializer(serializers.Serializer):
    data = serializers.JSONField(default={
        'chart':{}
    })

class ArtistCharSerializer(serializers.Serializer):
    pass


 
class Music(object):
    def __init__(self, id):
        self.id = id


class recommandSerializer(serializers.Serializer):
    recommandation = serializers.CharField(max_length=100)
