from django.urls import path
from . import views

urlpatterns = [
    path('chart/music', views.MusicChartView.as_view()),
    path('search/<int:user_id>/<str:keyword>', views.Search.as_view()),
    path('recommand/artist/<str:user_id>', views.RecommendArtist.as_view()),
    # path('chart/artist', views.ArtistChartView.as_view()),
    # path('search/<str:artist>', views.SearchArtist.as_view()),
]