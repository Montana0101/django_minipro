from django.http import HttpResponse,JsonResponse
from spider.book.index import fetch_books
import json
def spider_book(request):
    # print(request.GET.get('keyword'))
    keyword = request.GET.get('keyword')
    data = fetch_books(keyword)
    response = JsonResponse(data, safe=False)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response
    pass