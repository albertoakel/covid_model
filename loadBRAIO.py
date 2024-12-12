#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:11:59 2020

@author: akel
"""
#Programa para leitura dos dados covid19 disponibilizado pelo
#portal Brasil IO

import requests
import numpy as np
from datetime import datetime




def read_city(cidade,estado):
    
    url_city='https://brasil.io/api/dataset/covid19/caso_full/data?city='+cidade+'&city_ibge_code=&date=&format=json&is_last=&place_type=city&search=&state='+ estado

#    url_state='https://brasil.io/api/dataset/covid19/caso_full/data?city=&city_ibge_code=&date=&format=json&is_last=&place_type=state&search=&state='+ estado
    r = requests.get(url_city)
    data = r.json()
    
    NL=len(data['results'])
    C=np.zeros(NL);
    D=np.zeros(NL);
    NC=np.zeros(NL);
    ND=np.zeros(NL);
    C100=np.zeros(NL);
    date=np.zeros(NL,dtype=datetime);
    for i in range(NL):
        C[i]=data['results'][i]['last_available_confirmed'] #casos_acumulados
        D[i]=data['results'][i]['last_available_deaths']    #Mortes_acumuladas
        NC[i]=data['results'][i]['new_confirmed']
        ND[i]=data['results'][i]['new_deaths']
        C100[i]=data['results'][i]['last_available_confirmed_per_100k_inhabitants']
        data_str=data['results'][i]['last_available_date']
        date[i]=datetime.strptime(data_str,'%Y-%m-%d')
    return C,D,NC,ND,C100,date