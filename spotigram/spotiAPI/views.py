from django.shortcuts import render
from django.views.generic import ListView 
from rest_framework.views import APIView
from django.http import JsonResponse 
from rest_framework.response import Response
import sys, os
# sys.path.append('.ML')
# from .ML.ds import *
from .data import getMusicChart
from .serializers import (
    MusicChartSerializer, 
    Music, 
    recommandSerializer, 
    searchSerializer
    )
from instaAPI.models import User
from .search import *
# Create your views here.


class MusicChartView(APIView):
    def get(self, request):
        chart = getMusicChart()
        # data = MusicChartSerializer(chart, many=True).data
        return Response(chart)
 

# class getRecommand(APIView):
#     def get(self, request): #request는 dict형식으로 아니 그냥 모델에서 가져오자
#         # query = User.recent_music[:10]
#         query = request.data.values # iter dict 전달
#         recommand_list = []
#         for q in query:
#             rec = ds.recommend(q) # 최근 음악 1개당 비슷한거 3개 추천받음
#             for r in rec:
#                 recommand_list.append(r)

#         recommand_list = list(set(recommand_list)) # 중복되는 원소 제거
#         s_data = []
#         for r in recommand_list:
#             s_data.append(Music(id=r))
#         serializer = recommandSerializer(s_data, many=True)
#         return Response(serializer.data)
        
        
class Search(APIView):
    def get(self, request, user_id, keyword):
        search = keyword
        artist = get_artist(search)
        
        album = get_album(search)
        for a in album:
            del a['available_markets']

        track = get_track(search)
        # for t in track:
        #     del t['album']["available_markets"]
        
        result = {
            "artist":artist,
            "album":album,
            "track":track
        }
        '''
        recent_search = models.JSONField(default={'keyword': ''})
        recent_music = models.JSONField(default={'id': ''})
        recent_artist = models.JSONField(default={'id': ''})
        '''
        # 최근에 들은 음악..
        Usr = User.objects.get(id=user_id)
        Usr.recent_search.append({'keyword':search})
        for t in track:
            Usr.recent_music.append({'id':t['id']})
        for a in artist:
            Usr.recent_artist.append({'id':a['id']})
        Usr.save()
        # print(result)
        serializer = searchSerializer(result, many=True)
        # return Response(serializer.data)
        return Response(result)


class RecommendArtist(APIView):
    def get(self, request, user_id):
        Usr = User.objects.get(id=user_id)
        recent_artist = User.recent_artist[:3]
        recc = []
        for r in recent_artist:
            rid = r['id']
            rec = recommendation_for_artist_by_model(rid)['recommendations']
            for rc in rec:
                recc.append(rc)
        return Response({'recommendation':recc})






