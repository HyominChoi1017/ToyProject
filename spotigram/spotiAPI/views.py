from django.shortcuts import render
from django.views.generic import ListView 
from django.http import JsonResponse
from .data import getMusicChart
# Create your views here.


class MusicChartView(ListView):
    def get(self, request):
        return JsonResponse(getMusicChart())

class ArtistChartView(ListView):
    def get(self, request):
        return JsonResponse(getMusicChart())
