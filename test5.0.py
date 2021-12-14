#-*- codeing = utf-8 -*-
#@Time :2020/9/6 20:37
#@Author : zzf
#@File : test5.0.py
#@software: PyCharm Community Edition
import sys
import os
import re
import xlwt
import urllib.error,urllib.request
from bs4 import BeautifulSoup
import sqlite3
#
# findlink =re.compile(r'<a href="(.*?)">')#创建正则表达式对象，表示规则连接
# findImgScr=re.compile(r'<img.*src="(.*?)"',re.S)#处理换行符图片
# findTitle=re.compile(r'<span class="title">(.*)</span>')#名字
# findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')#评分
# findJudge=re.compile(r'<span>(\d*)人评价</span>')
# findInq=re.compile(r'<span class="inq">(.*)</span>')#概况
# findBd=re.compile(r'<p class="">(.*?)</p>',re.S)#相关neirong

url="https://www.23wx.cc/du/153/153206/40279501.html"
head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400"}
request=urllib.request.Request(url,headers=head)
html=""
try:
	response=urllib.request.urlopen(request)
	html=response.read().decode("gbk")
	#print(html)
except urllib.error.URLError as e:
	if hasattr(e,"code"):
		print(e.code)
	if hasattr(e,"reason"):
		print(e.reason)
# print(html)
print(type(html))
item=str(html)
findImgScr=re.compile(r'<a href="(.*?)" target="_blank">沧元图</a>')
imgSrc=re.findall(findImgScr,item)[0]
print(imgSrc)