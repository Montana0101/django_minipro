from django.urls import path
from .views import Weather,UserInfo
from django.views.generic import View

urlpatterns = [
   path('weather',Weather.as_view()),
   path('user',UserInfo.as_view())
]