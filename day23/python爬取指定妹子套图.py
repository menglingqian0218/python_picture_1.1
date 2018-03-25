#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests,time,os
from lxml import html

local_path ='D:\Program Files (x86)\爬虫\meizitu\\'
#输入套图标题，在本地创建套图标题文件夹
alt=input("请输入标题：")
os.mkdir(local_path+'{}'.format(alt))

#套图页面浏览器网址最后的几个数字
fanhao = input("请输入番号：")
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Host':'www.mmjpg.com',
'Referer':'http://www.mmjpg.com/mm/1262/2',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

url='http://www.mmjpg.com/mm/' + fanhao
response = requests.get(url,headers=headers).content
selector = html.fromstring(response)
image_amount = selector.xpath("//div[@class='page']/a[last()-1]/text()")[0]
image_amount=int(image_amount)
max_picture = image_amount+1
#打印套图有几张
print (max_picture)

#存储套图到本地套图标题文件夹，根据套图是18年还是17年的，修改下面f1里面的图片网址2018或者2017
for i in range(1,max_picture):
    with open('D:\Program Files (x86)\爬虫\meizitu\%s\%s.jpg' % (alt,i), 'wb') as f:
        f1 = requests.get(url='http://img.mmjpg.com/2018/%s/%s.jpg' % (fanhao,i),headers=headers).content
        f.write(f1)
