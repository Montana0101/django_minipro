import requests 
import json
from lxml import etree
from dd import spider_books as dd_books_spider
from jd import spider_books as jd_books_spider

def spider_books(book):
    data=[]
    text = requests.get('https://s.taobao.com/search?q=9787115546081&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210126&ie=utf8').text
    _html=etree.HTML(text)
    # title = _html.xpath('//img[@id="J_Itemlist_Pic_628873127371"]/@alt')
    # for i,v in title:
    #     print('吗大撒大撒',v)
    print('第三代凯撒',text)
    return  


if __name__ == '__main__':
    spider_books('python从零开始')
    