# -*- coding: utf-8 -*-
from django.http import HttpResponse
import requests
import json

def get_price(price):
    price = float(price)
    price = ('%.2f' % price).replace(".","")
    price = '0'*(7-len(price)) + price
    return price+'0'

def getlastprice(request):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer YOUR_AUTHORIZATION_TOKEN_HERE',
    }

    strike = request.GET.get('strike')
    symbol = request.GET.get('symbol').toupper()
    expiration = request.GET.get('expiration')
    call_or_put = request.GET.get('call_or_put').toupper()
    ###################################
    c_or_p = 'C' if call_or_put == 'CALL' else 'P'
    yy=expiration.split('-')[2][2:]
    mm=expiration.split('-')[0]
    dd=expiration.split('-')[1]
    formatted_strike = get_price(strike)
    complete_symbol = symbol+yy+mm+dd+c_or_p+formatted_strike
    params = (
        ('symbols', complete_symbol),
    )
    result = requests.get('https://sandbox.tradier.com/v1/markets/quotes', headers=headers, params=params)
    last_price = json.loads(result.text)['quotes']['quote']['last']
    return HttpResponse("<ol><li>"+str(last_price)+"</li></ol>")

