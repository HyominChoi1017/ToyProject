from django.urls import path
from .views import Register, Login

urlpatterns = [
    path('Register/', Register.as_view()),
    path('Login/', Login.as_view()),
]