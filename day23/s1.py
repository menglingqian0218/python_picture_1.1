#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/21
import requests
from bs4 import BeautifulSoup

response = requests.request(method='get',url='http://www.biquzi.com/2_2016/1189892.html')
response.encoding='gbk'
print (response.text)

soup = BeautifulSoup(response.text,'html.parser')
tag = soup.find(name='div',attrs={'id':'content'})
print (tag)

li_list = tag.find_all('li')
print (li_list)
for li in li_list:
    h3 = li.find(name='h3')
    if h3:
        print (h3.text)

with open('a.txt','a') as f:
    f.write(h3.text)