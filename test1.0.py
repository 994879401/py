#-*- codeing = utf-8 -*-
#@Time :2020/8/7 23:05
#@Author: zzf
#@File : test1.0.py
#@Software: PyCharm Community Edition

#-*- codeing = utf-8 -*-
#@Time :${DATE} ${TIME}
#@Author : zzf
#@File : ${NAME}.py
#@software: ${PRODUCT_NAME}
#
#提示




# #####https://pypi.tuna.tsinghua.edu.cn/simple/
#####清华镜像网站

#     阿里云 http://mirrors.aliyun.com/pypi/simple
#   豆瓣(douban) http://pypi.douban.com/simple
#   清华大学 https://pypi.tuna.tsinghua.edu.cn/simple
#   中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple
#     华中科技大学：http://pypi.hustunique.com/
#     山东理工大学：http://pypi.sdutlinux.org/

#pyinstaller -F ...py


#########################anaconda
# https://blog.csdn.net/weixin_43593330/article/details/102616023
#
# 添加可用的channel
# 4.1 pip安装
# 使用方法为加-i 加url，如下（以安装sklearn为例）：
#
#  pip install -U scikit-learn -i http://pypi.douban.com/simple
# 1
# 有时会报错，说
#
# The repository located at pypi.douban.com is not a trusted or secure host and is being ignored. If this repository is available via HTTPS we recommend you use HTTPS instead, otherwise you may silence this warning and allow it anyway with '–trusted-host pypi.douban.com’.
#
# 此时请按照提示输入如下命令：
#
# pip install -U scikit-learn -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
#

# pip install -U WordCloud -i http://pypi.douban.com/simple --trusted-host pypi.douban.com



# 4.2conda安装
# 如果是使用conda来安装， 执行这两条命令，可以将国内镜像源加入config文件
#
# conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# conda config --set show_channel_urls yes
# # 从channel中安装包时显示channel的url，这样就可以知道包的安装来源了。

# 然后再执行即可
#
# conda install scikit-learn

# D:\Program Files\MongoDB\Server\4.2\bin>mongod.exe --dapath D:\Program Files\MongoDB\Server\4.2\data\db

# pip install wordcloud -i https://pypi.doubanio.com/simple
# pip install pyqt5  -i https://pypi.tuna.tsinghua.edu.cn/simple
##################################################输出与看关键字
# print("hello,world")
# i=5
# print(i)
# import keyword
# print(keyword.kwlist)

# s=2
# print("1+1=%d"%s)
# y=1
# print("%d+1=%d"%(y,s))
# print("%s"%("小米"))
#
#
# print("www","baidu","com")
# print("www","baidu","com",sep=".")
#
##########################################################换行列
# print("world",end="")
# print("world",end="\t")
# print("python",end="\n")
# print("end")
#########################################################输入输出与类型
# password=input("请输入密码：")
# print("输出密码：",password)
#0
# m=input("输入：")
# print(type(m))
# m=int(m)
# print(type(m))
# print("%d"%(m))
#
############################################################if else的使用
# if True:
#     print("True")
# else:
#     print("Flase")
# print("end")
############################################################循环
# for i in range(5):
#     print(i)
# print("-------------")
# for i in range(0,10,3):
#     print(i)
# print("-------------")
# for i in range(0,11,3):
#     print(i)
# print("-------------")
#
#
############################################################字符
# str="chengdu"
# print(str[0])
# print(str[0:5])
# print(str[0:5:2])
# print(str[5:])
#

# i=0
# while i <5:
#     print (i+1)
#     i+=1
#
# i=0
# s=0
# while i <100:
#     i += 1
#     s=s+i
# print (s)
#


# i=0
# while i<10:
#     i+=1
#     if i==5:
#         continue
#     print (i)
#
#
# i=0
# while i<10:
#     i+=1
#     if i==5:
#         break
#     print (i)


# for i in range(1,10):
#     for j in range(1,10):
#         print("%d*%d=%d" % (i, j,i*j),end="\n")

##########################################################99乘法
# i=0
# while i <9:
#     while 1:
#         i += 1
#         j = 0
#         while j < i:
#             while 1:
#                 j += 1
#                 print("%d*%d=%d" % (i, j, i * j), end="  ")
#                 break
#         print ()
#         break



#############################################################列表
#####################增
#  list=[1,3,5,7]
# for i in list:
#     print (i)
# list.append(5)
# print (list)
#
# a=[1,2]
# b=[3,4]
# a.append(b)
# print(a)
#
# a.extend(b)
# print (a)
#
# l=[0,1,2]
# l.insert(1,3)
# print (l)
#########################3删除
# m=[1,3,8,4,5,4,6,4]
# del m[2]
# print (m)
# m.pop()
# print (m)
# m.remove(4)
# print (m)

# n=[1,3,8,4,5,9]
# n[1]=7
# print (n)

#####################查找
#
a=[1,3,5,7,9]
print (a.index(1,0,3))#在列表a的第1个到第3个元素中找1的下标

print (a.count(1))#a中1出现次数
####################
a=[1,3,7,5,9]
a.reverse()####反转
print (a)
a.sort()####排序
print (a)
a.sort(reverse=True)#####降序
print (a)

#################嵌套
s_list=[["清华大学","北京大学"],["浙江大学","中山大学"],["南昌大学","福建大学"]]
print (s_list[0])
print (s_list[0][0])

l_list=['A','B','C','D','E','F','G','H']
t_list=[[],[],[]]
print (l_list)
import random

for i in l_list:
    index = random.randint(0, 2)
    t_list[index].append(i)

i=1
for j in t_list:
    print ("办公室%d 的人数： %d"%(i,len(j)))
    i+=1
    for name in j:
        print ("%s"%name,end="\t")
    print("\n")
    print ("-"*20)









import pandas
import sys
import os
import re
import xlwt
import urllib.error,urllib.request
from bs4 import BeautifulSoup
import sqlite3


