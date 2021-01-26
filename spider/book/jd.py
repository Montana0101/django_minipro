from lxml import etree
import requests 
import json

def spider_books(book):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh;q=0.3',
        'Referer': 'https://www.jd.com/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
    }
    text = requests.get('https://search.jd.com/Search?keyword={0}'.format(book),headers=headers).text
    _html = etree.HTML(text)
    _ul = _html.xpath('//*[@id="J_searchWrap"]//ul/li//i/text()')

    price = _html.xpath('//*[@class="p-price"]//i/text()')
    author = _html.xpath('//div[@class="p-bookdetails"]/span[@class="p-bi-name"]/a[1]/text()')
    store = _html.xpath('//div[@class="p-bookdetails"]/span[@class="p-bi-store"]/a[1]/text()')
    title = _html.xpath('//div[@class="p-name"]//em/text()')
    urls = _html.xpath('//*[@class="p-img"]/a/@href')
    img = _html.xpath('//*[@class="p-img"]//img/@data-lazy-img')

    data = []
    obj_response = {}
    for i,v in enumerate(title):
        try :
            obj_response['title'] = v
            obj_response['price'] = price[i]
            obj_response['store'] = store[i]
            obj_response['author'] = author[i]
            obj_response['url'] = "https:"+urls[i]
            obj_response['img'] = "https:"+img[i]
            obj_response['source'] = '京东'
            data.append(obj_response)
        except:
            # print('遍历失败系列',v)
            pass
        pass
    return data
    pass

if __name__ == '__main__':
    spider_books()
    
