from django.http import HttpResponse,JsonResponse
from django.views import View
from utils.weather import search_weather
from . import models

import json
import datetime

def hello(request):
    now = datetime.datetime.now()
    html = '<html><body>NOW IS %s</body></html>' % now
    return HttpResponse(html)

class Weather(View):
    def get(self,request):
        city = request.GET['city']
        res = search_weather(city)
        return HttpResponse(json.dumps(res),content_type='application/json')
    
    def post(self,request):
        return HttpResponse('POST业务请求')

    def put(self,request):
        return HttpResponse("PUT业务请求")

    def delete(self,request):
        return HttpResponse('DELETE业务请求')
    pass

class UserInfo(View):
    def get(self,request):
        pass

    def post(self,request):
        body = request.body.decode()
        result_data = json.loads(body)
        openid = result_data['openid']
        wechat_name = result_data['wechat_name']
        wechat_photo = result_data['wechat_photo']
        mobile = result_data['mobile']
        address = result_data['address']
        register_response = {}
        if openid :
            register_response['code'] = 0 
            register_response['msg'] = '注册成功'
            register_response['info'] = result_data
            try :
                models.User.objects.create(**result_data)
            except :
                register_response['code'] = -1
                register_response['msg'] = 'openid已存在或手机号已注册'
        else :
            register_response['code'] = -1 
            register_response['msg'] = '没有openid, 注册失败'
        return HttpResponse(json.dumps(register_response),content_type='application/json')
        pass