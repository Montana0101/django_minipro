class Basic:
    # weather_api = 'http://apis.juhe.cn/simpleWeather/query'  聚合
    weather_api = 'https://service-1gxue92k-1301115409.gz.apigw.tencentcs.com/release/' #腾讯

    secretId = "AKIDiwtbingnmk6pienpspgbr0lg50antt4tt6er"
    secretKey = "Brz8G8rP2q2jyjrCt9KlAd27phoBioaBgDTzqna7"

    # weather_key_juhe = 'b28631a343502616434a0ccf8f75ad17'

    appid='wx2e737b101ab26f88'
    appsecret='ce667216f49f377728e37febf56d7f94'
    weachat_openid_url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&grant_type=authorization_code' %(appid,appsecret)

     