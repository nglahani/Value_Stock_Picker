# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 15:15:10 2019
Collects Stock Data on All Available Entities in SimFin DataBase

@author: Niko Lahanis
"""

import requests

api_key="mwQjjLorlcNiWr3Oi9O3G0nQDDz6s4Mc"

uRL = "https://simfin.com/api/v1/info/all-entities?api-key={}".format(api_key)
response = requests.get(uRL)
data = response.json()
print(data)

