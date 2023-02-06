from django.urls import path
from .views import Register, Login, UserUpdate,PlaySearch

urlpatterns = [
    path('Register/', Register.as_view()),
    path('Login/', Login.as_view()),
    path('UserUpdate/', UserUpdate.as_view()),
    path('PlaySearch/', PlaySearch.as_view()),
]