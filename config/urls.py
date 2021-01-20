from django.contrib import admin
from django.urls import path,include
from apis import urls as app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(app_urls)),
]
