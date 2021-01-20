
import json
import sys
sys.path.append('..')

from django.http import HttpResponse,JsonResponse
from django.views import View
# from utils.weather import search_weather

from .. import models


class Weather(View):
    def get(self,request):
        # city = request.GET['city']
        # res = search_weather(city)
        # return HttpResponse(json.dumps(res),content_type='application/json')
    
    def post(self,request):
        return HttpResponse('POST业务请求')

    def put(self,request):
        return HttpResponse("PUT业务请求")

    def delete(self,request):
        return HttpResponse('DELETE业务请求')
    pass