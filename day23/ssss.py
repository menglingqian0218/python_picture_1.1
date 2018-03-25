#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/25

# coding:utf-8
import requests
from lxml import html
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Referer':'http://www.mmjpg.com/home/4'}
for p in range(2,3):
    url='http://www.mmjpg.com/home/' + str(p)
    response = requests.get(url,headers=headers).text
    selector = html.fromstring(response)
    image_amount = selector.xpath("//div[@class='pic']/ul/li/a/img/@src")
    alt=[]
    for a in image_amount:
        alt.append(a)


        l_tmp = l.split('/')[-1].split('.')[0]
        l_list.append(l_tmp)
    print (l_list)
    #print (response)a
    #print (image_amount)







