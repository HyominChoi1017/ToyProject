from django.shortcuts import render
from django.views.generic import ListView 
from rest_framework.views import APIView
from django.http import JsonResponse 
from rest_framework.response import Response
from .data import getMusicChart
from .serializers import MusicChartSerializer
# Create your views here.


class MusicChartView(APIView):
    def get(self, request):
        chart = getMusicChart()
        # data = MusicChartSerializer(chart, many=True).data
        return Response(chart)
