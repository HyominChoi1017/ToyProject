from django.shortcuts import render
from django.views.generic import ListView 
from rest_framework.views import APIView
from django.http import JsonResponse 
from rest_framework.response import Response
from ML.ds import recommend
from .data import getMusicChart
from .serializers import MusicChartSerializer, Music, recommandSerializer
from instaAPI.models import User
# Create your views here.


class MusicChartView(APIView):
    def get(self, request):
        chart = getMusicChart()
        # data = MusicChartSerializer(chart, many=True).data
        return Response(chart)
 

class getRecommand(APIView):
    def get(self, request): #request는 dict형식으로 아니 그냥 모델에서 가져오자
        # query = User.recent_music[:10]
        query = request.data.values # iter dict 전달
        recommand_list = []
        for q in query:
            rec = recommend(q) # 최근 음악 1개당 비슷한거 3개 추천받음
            for r in rec:
                recommand_list.append(r)

        recommand_list = list(set(recommand_list)) # 중복되는 원소 제거
        s_data = []
        for r in recommand_list:
            s_data.append(Music(id=r))
        serializer = recommandSerializer(s_data, many=True)
        return Response(serializer.data)
        
        


