from config.const import Basic 
from django.utils import timezone
from datetime import datetime as pydatetime
import ssl, hmac, base64, hashlib
import requests

timestamp = timezone.now()

try:
    from urllib import urlencode
    from urllib2 import Request, urlopen
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen

def search_weather(city):
        # 签名
        source = "market"
        datetime = pydatetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        signStr = "x-date: %s\nx-source: %s" % (datetime, source)
        sign = base64.b64encode(hmac.new(Basic.secretKey.encode('utf-8'), signStr.encode('utf-8'), hashlib.sha1).digest())
        auth = 'hmac id="%s", algorithm="hmac-sha1", headers="x-date x-source", signature="%s"' % (Basic.secretId, sign.decode('utf-8'))

        # 请求头
        headers = {
            'X-Source': source,
            'X-Date': datetime,
            'Authorization': auth,
        }

        # 查询参数
        queryParams = {
            'area': '',
            'city': city,
            'code': '',
            'district': '',
            'ip': '',
            'lat': '',
            'lng': '',
            'region': ''}

        # body参数（POST方法下存在）
        bodyParams = {
        }

        url = Basic.weather_api
        if len(queryParams.keys()) > 0:
             url = url + '?' + urlencode(queryParams)

        response = requests.get(url,headers=headers).json()
        result = {
            'code': 0,
            'data':{}
        }
        res_code = response['code']
        response = response['data']

        if res_code == 0 :
            result['code'] = 0
            result['data']['province'] = response['location']['region']
            result['data']['city'] = response['location']['city']
            result['data']['area'] = response['location']['district']
            result['data']['realdata'] = response['realtime']
            result['data']['present'] = response['24hoursForecast']
            result['data']['weekend'] = response['7daysForecast']
        else:
            result['code'] = -1
            result['data'] = None

        return result

