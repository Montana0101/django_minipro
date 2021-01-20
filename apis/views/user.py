import json
import requests

from django.http import HttpResponse,JsonResponse
from django.views import View
from apis.models import User
from config.const import Basic


class UserInfo(View):
    def get(self,request):
        pass

    def post(self,request):
        result_data = json.loads(request.body.decode())
        openid = result_data['openid']
        # 返回数据
        register_response = {}
        if 'wechat_name' in result_data:
            wechat_name = result_data['wechat_name']
        if 'wechat_photo' in result_data:
            wechat_photo = result_data['wechat_photo']
        if 'mobile' in result_data:
            mobile = result_data['mobile']
        if 'address' in result_data:
            address = result_data['address']
        if 'gender' in result_data:
            gender = result_data['gender']
        if 'openid' in result_data:
            openid = result_data['openid']
            try :
                User.objects.create(**result_data)
                register_response['code'] = 0 
                register_response['message'] = '注册成功'   
            except :
                register_response['code'] = -1
                register_response['message'] = '用户已存在或手机号已注册'
        else :
            register_response['code'] = -1 
            register_response['message'] = '未找到openid，注册失败'
        return HttpResponse(json.dumps(register_response),content_type='application/json')
        pass
    
    def put(self,request):
        print('更新用户信息')
        pass

    def delete(self,request):
        _data = json.loads(request.body.decode())
        openid = _data['openid']
        delete_result = {}
        is_exist = User.objects.filter(openid=openid)
        if is_exist:
            try:
                User.objects.filter(openid=openid).delete()
                delete_result['code'] = 0
                delete_result['message'] = '删除成功'
            except:
                delete_result['code'] = -1
                delete_result['message'] = '异常情况，删除失败'
        else:
            delete_result['code'] = -1
            delete_result['message'] = '未找到用户信息，删除失败'
        return HttpResponse(json.dumps(delete_result),content_type='application/json')
        pass

    def fetchOpenId(self,request):
        if request.method == 'POST':
            bodydata = request.body
            print('打印下',bodydata)
        return HttpResponse(json.dumps(bodydata))

class UserAuth(View):
    def post(self,request):
        user_code = json.loads(request.body)['code']
        auto_url = Basic.weachat_openid_url + '&js_code=%s'%user_code
        auto_response = requests.get(auto_url).json()
        _response_data = {}
        if auto_response['openid'] :
            print('测试')
            _response_data['code'] = 0 
            _response_data['message'] = '成功获取openid'
            _response_data['data'] = auto_response
        else :
            print('错误')
            _response_data['code'] = -1 
            _response_data['message'] = '获取openid失败'
        return HttpResponse(json.dumps(_response_data),content_type='application/json')
        pass
