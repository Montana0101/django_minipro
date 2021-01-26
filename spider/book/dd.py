from lxml import etree
import requests 
import json

def spider_books(book):
    # json格式化
    data = []
    # 当当网
    text = requests.get('http://search.dangdang.com/?key={}&act=input'.format(book)).text
    _html = etree.HTML(text)
    _arr = _html.xpath('//div[@id="search_nature_rg"]/ul/li/p[@class="name"]/a[@title]/text()')
    title = _html.xpath('//div[@id="search_nature_rg"]/ul/li/a/@title')
    urls = _html.xpath('//div[@id="search_nature_rg"]/ul/li/a/@href')
    author = _html.xpath('//div[@id="search_nature_rg"]/ul/li/p[@class="search_book_author"]/span[1]/a/text()')
    store = _html.xpath('//div[@id="search_nature_rg"]/ul/li/p[@class="search_book_author"]/span[last()]/a/text()')
    price = _html.xpath('//div[@id="search_nature_rg"]/ul/li/p[@class="price"]/span[@class="search_now_price"]/text()')   
    imgs = _html.xpath('//div[@id="search_nature_rg"]/ul/li//a[@name="itemlist-picture"]/img/@data-original')
    for index,item in enumerate(title) :
        try:
            books_obj = {}
            books_obj['name'] = item.strip()
            books_obj['price'] = price[index].replace('¥','')
            books_obj['author'] = author[index]
            books_obj['store'] = store[index]
            books_obj['url'] = urls[index]
            books_obj['img'] = imgs[index]
            books_obj['source'] = '当当网'
            data.append(books_obj)
        except:
            # print('打印下错误 %s'%(item))
            pass
    return data
    pass

if __name__ == '__main__':
    spider_books()
    