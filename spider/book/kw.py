import requests
import json 
from lxml import etree 

def spider_books(book):
    headers={
        'Host':'search.kongfz.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }
    text = requests.get('https://search.kongfz.com/product_result/?key={}&ajaxdata=1&type=1&quality=100'.format(book),headers=headers)
    text.encoding='utf-8'
    text = json.loads(text.text)
    data = text['data'] 
    result = data['itemList']
 
    response_data = []
    for i,v in enumerate(result):
        obj = {}
        obj['title'] = v['itemname']
        obj['author'] = v['author']
        obj['store'] = v['press']
        obj['img'] = v['bigimgurl']
        obj['price'] = v['price']
        obj['source'] = '孔夫子旧书网'
        obj['url']='http://book.kongfz.com/{0}/{1}'.format(v['shopid'],v['itemid'])
        response_data.append(obj)
        # print('打印下每一条',obj)
        pass
    return response_data