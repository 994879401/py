import plotly
import sys
import os
import re
import xlwt
import urllib.error,urllib.request
import sqlite3
import pandas
from bs4 import BeautifulSoup
import requests
import jieba        #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud         #词云
from PIL import Image                   #图片处理
import numpy as np                      #矩阵运算
import sqlite3                          #数据库
import pymongo
import openpyxl
from bs4 import BeautifulSoup
import requests

# url1 = 'https://www.xinshuhaige.com/44733/'
# # m = 536830O
# m=537157
# while m <= 537500:
#     url = url1 + str(m) + '.html'
#     print(url)
#     response = requests.get(url=url)
#     with open('./dsj/%d.html' % (m), 'w', encoding='utf-8')as fp:
#         fp.write(response.text)
#         print("%s已保存"%(url))
#         fp.close()
#     m += 1
# print("全部")
#
#
#
#
#
#
#
#
#
#
#
#
#
