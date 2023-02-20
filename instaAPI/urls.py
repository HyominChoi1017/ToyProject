from django.urls import path
from .views import *

urlpatterns = [
    path('Register/', Register.as_view()),
    path('Login/', Login.as_view()),
    path('UserUpdate/', UserUpdate.as_view()),
    path('PlaySearch/', PlaySearch.as_view()),
    path('PlayCreate/', PlayCreate.as_view()),
    path('PlayRead/', PlayRead.as_view()),
    path('PlayUpdate/', PlayUpdate.as_view()),
    path('PlayDelete/', PlayDelete.as_view()),

    #    path('Post/', PostView.as_view()),
#    path('Post/<int:post_id>', SinglePostView.as_view()),
#    path('Comment/<int:post_id>', CommentView.as_view()), # 특정 게시글에 대한 댓글을 보여준다.
#    path('User/<int:user_id>', UserView.as_view()), # get single userdata
]