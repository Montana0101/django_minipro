from django.urls import path
from .views import user,weather,spider
from django.views.generic import View

urlpatterns = [
   path('user',user.UserInfo.as_view()),
   path('user/openid',user.UserAuth.as_view()),
   path('weather',weather.WeatherInfo.as_view()),
   path('spider/books',spider.spider_book)
]