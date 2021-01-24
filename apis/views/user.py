import json
import requests

from django.http import HttpResponse,JsonResponse
from django.views import View
from apis.models import User
from config.const import Basic


class UserInfo(View):
    def get(self,request):
        openid = None
        search_res = {}
        if 'openid' in request.GET:
            openid = request.GET['openid']
            try :
                search_data = User.objects.get(openid=openid)
                search_data = search_data.__dict__

                filter_data = dict((key,value) for key,value in search_data.items() 
                if key=='mobile' or key=='wechat_name' or key=='openid' or key=='wechat_photo'
                or key=='address' or key=='gender' or key=='province' or key=='city' or key=='area')
                
                search_res['data'] = filter_data
                search_res['code'] = 0
                search_res['message'] = '查询成功'
            except:
                search_res['code'] = -1
                search_res['message'] = '未找到该用户，查询失败'
        else :
            search_res['code'] = -1
            search_res['message'] = '传参错误，查询失败'
        return HttpResponse(json.dumps(search_res),content_type='application/json')

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
            register_response['message'] = '未收到openid，注册失败'
        return HttpResponse(json.dumps(register_response),content_type='application/json')
        pass
    
    def put(self,request):
        request_data = json.loads(request.body)
        _openid = request_data['openid']
        update_res = {}
        if 'openid' in json.loads(request.body):
            update_filter_data= dict((key,value) for key,value in request_data.items() if key != 'openid')
            print('过滤掉Openid',update_filter_data)
            try :
                update_one = User.objects.get(openid=_openid)
                update_result = update_one.__dict__.update(**update_filter_data)
                update_one.save()  # 注意
                update_res['code'] = 0
                update_res['message'] = '更新成功'
                # update_res['data'] = update_result
            except:
                update_res['code'] = -1
                update_res['message'] = '查询报错，更新失败'              
        else :
            print('没有Openid')
            update_res['code'] = -1
            update_res['message'] = '未收到openid，更新失败'
            

        return HttpResponse(json.dumps(update_res),content_type='application/json')
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
