#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/3/3

import requests,time,os
from lxml import html

with open(r'D:\Program Files (x86)\爬虫\meizitu\美女主播私房写真秀曼妙的身材美如画\2.jpg','wb') as f:
    f1 = requests.get(url='http://img.mmjpg.com/2018/1262/2i12.jpg').content
    f.write(f1)
