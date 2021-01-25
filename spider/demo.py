from lxml import etree
import requests 
import json



def books_from_dangdang(book):
    # json格式化
    data = []
    # 当当网
    text = requests.get('http://search.dangdang.com/?key={}&act=input'.format(book)).text
    _html = etree.HTML(text)
    _arr = _html.xpath('//div[@id="search_nature_rg"]/ul/li/p[@class="name"]/a[@title]/text()')
    title = _html.xpath('//div[@id="search_nature_rg"]/ul/li/a/@title')
    urls = _html.xpath('//div[@id="search_nature_rg"]/ul/li/a/@href')
    author = _html.xpath('//div[@id="search_nature_rg"]/ul/li/p[@class="search_book_author"]/span[1]/a/text()')
    publish = _html.xpath('//div[@id="search_nature_rg"]/ul/li/p[@class="search_book_author"]/span[last()]/a/text()')
    price = _html.xpath('//div[@id="search_nature_rg"]/ul/li/p[@class="price"]/span[@class="search_now_price"]/text()')
   
    for index,item in enumerate(title) :
        try:
            books_obj = {}
            books_obj['name'] = item.strip()
            books_obj['price'] = price[index]
            books_obj['author'] = author[index]
            books_obj['publish'] = publish[index]
            books_obj['url'] = urls[index]
            books_obj['source'] = '当当网'
            data.append(books_obj)
        except:
            print('打印下错误 %s'%(item))
    return data
    pass

def books_from_jingdong(book,author):
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
    text = requests.get('https://search.jd.com/Search?keyword={0}&exp_key={1}'.format(book,author),headers=headers).text
    _html = etree.HTML(text)
    _ul = _html.xpath('//*[@id="J_searchWrap"]//ul/li//i/text()')
    name = _html.xpath('//*[@id="J_searchWrap"]//ul/li//div[@class="p-name"]//em//font//text()')
    price = _html.xpath('//*[@id="J_searchWrap"]//ul/li//div[@class="p-price"]//strong//i/text()')
    publish = _html.xpath('//*[@id="J_searchWrap"]//ul/li//div[@class="p-shopnum"]//a//text()')
    urls = _html.xpath('//*[@id="J_searchWrap"]//div[@class="p-name"]//a//@href')
    # author = _html.xpath('//*[@class="p-bi-name"]//a[1]/@title')
    author=author
    data = []
    obj_response = {}
    for i,v in enumerate(name):
        try :
            obj_response['name'] = v 
            obj_response['price'] = price[i]
            obj_response['publish'] = publish[i]
            obj_response['author'] = author[i]
            obj_response['url'] = "https:"+urls[i]
            obj_response['source'] = '京东网'
            data.append(obj_response)
        except:
            print('作者信息不详',v)
        pass
    return data
    pass

def spider_books(book,author):
    dd_arr = books_from_dangdang(book)
    jd_arr = books_from_jingdong(book,author)

    data = []
    for index,item in enumerate(dd_arr):
        if author in item['author'] :
            data.append(item)
        else :
            pass
    
    for index,item in enumerate(jd_arr):
        data.append(item)
        pass


    with open('demo.json','w',encoding='utf-8') as books_file:
        json.dump(data,books_file,ensure_ascii=False)
    pass


if __name__ == '__main__':
    spider_books('python编程:从入门到实践','埃')
    