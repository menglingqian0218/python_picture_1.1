#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/12/30

from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = '''重置密码 重置密码 重置密码 sb aaa  申请vms系统匹配流水 抬头错误  sb sb ws qw er e34 r54 
申请vms系统匹配流水 申请vms系统匹配流水 申请vms系统匹配流水 抬头错误 抬头错误 修改发票状态 修改发票状态 没有流水 没有流水 没有流水 修改发票状态 修改发票状态
发票金额不对 发票金额不对  修改销方地址 申请临时放开纳税人识别号限制 申请vms系统匹配流水
'''

# the font from github: https://github.com/adobe-fonts
#仿宋常规
font = r'C:\Windows\Fonts\simfang.ttf'
wc = WordCloud(collocations=False, background_color='white',font_path=font,width=2000, height=1500, margin=2).generate(text.lower())

plt.imshow(wc)
plt.axis("off")
plt.show()

wc.to_file('show_Chinese.png')
