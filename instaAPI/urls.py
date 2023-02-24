from django.urls import path
from .views import *

# urlpatterns = [
#     path('Register/', Register.as_view(), name='register'),
#     path('Login/', Login.as_view()),
#     path('UserUpdate/', UserUpdate.as_view()),
#     path('PlaySearch/', PlaySearch.as_view()),
#     path('PlayCreate/', PlayCreate.as_view()),
#     path('PlayRead/', PlayRead.as_view()),
#     path('PlayDelete/', PlayDelete.as_view()),
#     path('PlayUpdate/', PlayUpdate.as_view()),
# ]
from django.urls import path
from .views import RegisterView, LoginView, UserDetailView, PlaylistList, PlaylistDetail

urlpatterns = [
    path('Register/', RegisterView.as_view(), name='register'),
    path('Login/', LoginView.as_view(), name='login'),
    path('Userdate/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('playlists/', PlaylistList.as_view(), name='playlist-list'),
    path('playlists/<int:pk>/', PlaylistDetail.as_view(), name='playlist-detail'),
]
#    path('Post/', PostView.as_view()),
#    path('Post/<int:post_id>', SinglePostView.as_view()),
#    path('Comment/<int:post_id>', CommentView.as_view()), # 특정 게시글에 대한 댓글을 보여준다.
#    path('User/<int:user_id>', UserView.as_view()), # get single userdata
