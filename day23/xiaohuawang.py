from urllib import request
from bs4 import BeautifulSoup
import re
import requests
import urllib
path = '‪D:\Program Files (x86)\爬虫\校花网'
url = 'http://www.xiaohuar.com/list-1-{}.html'
class SchoolFlower(object):
    def __init__(self,url):
        self.url = url
        self.header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
        self.List = []
        self.Connection()

    def Connection(self):
        content = requests.get(self.url,headers=self.header)
        content.encoding = 'utf-8'
        soup = BeautifulSoup(content.content,'html.parser',from_encoding='gbk')
        return soup

    def Getpicture(self):
        info = self.Connection()
        img = info.find_all('img',src=re.compile(r'/d/file/\d+/\w+\.jpg'))
        x = 0
        for i in img:
            print('正在下载弟{}张照片'.format(x))
            f = open('D:\Program Files (x86)\爬虫\校花网\%s.jpg' % i.get('alt'),'wb')
            f1 = requests.get('http://www.xiaohuar.com%s' % i.get('src')).content
            f.write(f1)
            x += 1
        x = 0

for i in range(10,11):
    print('#########开始下载第{}页的图片##########'.format(i))
    f = SchoolFlower(url.format(i))
    f.Getpicture()