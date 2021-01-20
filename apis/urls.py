from django.urls import path
from .views import user
from django.views.generic import View

urlpatterns = [
   path('user',user.UserInfo.as_view()),
   path('user/openid',user.UserAuth.as_view())
]