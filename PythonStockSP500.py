# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 23:05:03 2019
Collects Stock Data on SP500 Entities in SimFin DataBase

@author: Niko Lahanis
"""

import requests
import bs4 as bs
import pickle

def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
    
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)
        
    return tickers

a=save_sp500_tickers()
api_key="mwQjjLorlcNiWr3Oi9O3G0nQDDz6s4Mc"


b=[]
for item in a:
    addToB=item[0:len(item)-1]
    b.append(addToB)

for item in b:
    uRL = "https://simfin.com/api/v1/info/find-id/ticker/{}?api-key={}".format(item,api_key)
    response = requests.get(uRL)
    data = response.json()
    print(data)
    simId=data[0].get('simId')




