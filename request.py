# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 15:21:23 2019

@author: murat
"""

import requests

url = "http://localhost:5000/predict_api"
r = request.post(url, json = {"krediMiktari" : 1200, "yas" : 70, "evDurumu" : 0, "aldigi_kredi_sayi" : 2, "telefonDurumu" : 1})

print(r.json())
 