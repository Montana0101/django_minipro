import requests 
import json
from lxml import etree
from .dd import spider_books as dd_books_spider
from .jd import spider_books as jd_books_spider
from .kw import spider_books as kw_books_spider


def fetch_books(book):
    dd_arr = dd_books_spider(book)
    jd_arr = jd_books_spider(book)
    kw_arr = kw_books_spider(book)

    data = []
    for index,item in enumerate(dd_arr):
        data.append(item)
    

    for index,item in enumerate(jd_arr):
        data.append(item)
        pass

    for index,item in enumerate(kw_arr):
        data.append(item)
        pass

    # 价格排序
    def sortedPrice(obj):
        return float(obj['price'])
    
    data.sort(key=sortedPrice)

    # with open('../json/book_data.json','w',encoding='utf-8') as books_file:
    #     json.dump(data,books_file,ensure_ascii=False)
    return data
    pass


if __name__ == '__main__':
    fetch_books('9787115546081')
    