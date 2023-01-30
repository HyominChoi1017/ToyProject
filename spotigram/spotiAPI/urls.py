from django.urls import path
from . import views

urlpatterns = [
    path('/chart/music', views.MusicChartView.as_view()),
    path('/chart/artist', views.ArtistChartView.as_view()),
    # path('search/<str:artist>', views.SearchArtist.as_view()),
]