from config.const import Basic 
from django.utils import timezone
import requests

timestamp = timezone.now()

def search_weather(city):
        url = Basic.weather_api+'?city=%s&key=%s'%(city,Basic.weather_key_juhe)
        response = requests.get(url).json()
        result = {
            'code': 0,
            'data':{}
        }
        if response['error_code'] == 0 :
            result['code'] = 0
            result['data']['cityname'] = response['result']['city']
            result['data']['realdata'] = response['result']['realtime']
            result['data']['weekdata'] = response['result']['future']

        else:
            result['code'] = -1
            result['data'] = None
        return result

