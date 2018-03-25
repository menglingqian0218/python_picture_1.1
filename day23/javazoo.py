#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/21


import requests,re,urllib.request
from bs4 import BeautifulSoup
#
for i in range(0,3):
    response = requests.request(method='get',url='http://www.xiaohuar.com/list-1-{}.html'.format(i))
    response.encoding='gb2312'
    print (response.text)
    soup = BeautifulSoup(response.text,'html.parser')
    tag = soup.find_all(name='div',attrs={'class':'a'})
    print(tag)
# with open('%s.jpg' %i,'wb') as f:
#     f.write(response.content)



