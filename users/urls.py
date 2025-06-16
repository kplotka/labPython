from django.urls import path
from .views import register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]