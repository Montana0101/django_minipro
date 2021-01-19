class Basic:
    weather_api = 'http://apis.juhe.cn/simpleWeather/query'
    weather_key_juhe = 'b28631a343502616434a0ccf8f75ad17'

if __name__=='__main__':
    _v = Basic()
    print('测试',_v.weather_key_juhe)