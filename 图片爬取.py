#-*- codeing = utf-8 -*-
#@Time :2020/9/8 17:57
#@Author : zzf
#@File : 图片爬取.py
#@software: PyCharm Community Edition



import requests
import os











import sys
import os
import re
import xlwt
import urllib.error,urllib.request
from bs4 import BeautifulSoup
import sqlite3

findlink =re.compile(r'<a href="(.*?)">')#创建正则表达式对象，表示规则连接
findImgScr=re.compile(r'<img.*src="(.*?)"',re.S)#处理换行符图片
findTitle=re.compile(r'<span class="title">(.*)</span>')#名字
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')#评分
findJudge=re.compile(r'<span>(\d*)人评价</span>')
findInq=re.compile(r'<span class="inq">(.*)</span>')#概况
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)#相关neirong

#爬取网页
def getData(baseurl):
	datalist=[]
	for i in range(0,1):
		url=baseurl+str(i*25)
		html=askURL(url)#保存获取到的一网页
		# 2,解析数据
		soup =BeautifulSoup(html,"html.parser")
		for item in soup.find_all('div',class_="item"):#查找数据
			data=[]  #保存一部电影的所有信息
			item=str(item)
			link =re.findall(findlink,item)[0]#获取连接

			data.append(link)
			imgSrc=re.findall(findImgScr,item)[0]
			imgSrc=str(imgSrc)

			data.append(imgSrc)
			titles=re.findall(findTitle,item)
			if(len(titles))==2:
				ctitle=titles[0]
				data.append(ctitle)
				otitle=titles[1].replace("/","")
				data.append(otitle)
			else:
				data.append(titles[0])
				data.append('')#外国名留空
			rating=re.findall(findRating,item)[0]#p评分
			data.append(rating)
			judge=re.findall(findJudge,item)[0]#评价人数
			data.append(judge)
			inq=re.findall(findInq,item)#概述
			if len(inq)!=0:
				inq=inq[0].replace("。","")
				data.append(inq)
			else:
				data.append("")
			bd=re.findall(findBd,item)[0]
			bd=re.sub('<br(\s+)?/>(\s+)?'," ",bd)#去br
			bd=re.sub('/',"",bd)
			data.append(bd.strip())
			datalist.append(data)

	# print(datalist)
	return datalist

#得到一个URL的网页内容
def askURL(url):
	head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400"}
	request=urllib.request.Request(url,headers=head)
	html=""
	try:
		response=urllib.request.urlopen(request)
		html=response.read().decode("utf8")
		#print(html)
	except urllib.error.URLError as e:
		if hasattr(e,"code"):
			print(e.code)
		if hasattr(e,"reason"):
			print(e.reason)
	return html


#保存数据
def saveData(datalist,savepath):
	import xlwt
	book=xlwt.Workbook(encoding="utf8",style_compression=0)
	sheet=book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)#=true是为了覆盖
	col=("电影链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
	for i in range(0, 8):
		# print(col[i])
		sheet.write(0, i, col[i])

	for i in range(0,250):
		print("第%d条"%(i+1))
		data=datalist[i]
		for j in range(0,8):
			sheet.write(i+1,j,data[j])
	book.save(savepath)
def saveData2DB(datalist,dbpath):
	# init_db(dbpath)
	# conn =sqlite3.connect(dbpath)
	# cur = conn.cursor()
	i=1
	for data in datalist:
		for index in range(len(data)):
			if index==4 or index==5:
				continue
			data[index] = '"'+data[index]+'"'
		# sql = '''
		#    insert into movie250(
		#    info_link,pic_link,cname,ename,score,rated,instroduction,info)
		#    values(%s)'''%",".join(data)
		# print(sql)

		# cur.execute(sql)
		# conn.commit()
		item=data[1]
		# print(item)
		findlink = re.compile(r'"(.*?)"')

		link = re.findall(findlink, item)[0]  ####获取连接
		# print(link)
		link=link[0:-3]+'webp'
		print(link)
		print(type(link))
		url="%s"%(link)
		print(url)

		# url = "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg"
















	# print(data[1])
		# url = data[1]
		# print(url)
		root = "D://pics//豆瓣图片//"
		path = root + url.split('/')[-1]
		print("第%d张图"%i)
		try:
			kv = {'q': 'keyword'}
			if not os.path.exists(root):
				os.mkdir(root)
			if not os.path.exists(path):
				r = requests.get(url, params=kv)
				with open(path, 'wb')as f:
					f.write(r.content)
					f.close()
					print("文件保存成功")
			else:
				print("文件已存在")
		except Exception as result:
			print(result)
		i+=1






	# cur.close()
	# conn.close()


def init_db(dbpath):
	sql='''
	create table movie250
	(
	id integer primary key autoincrement,
	info_Link text,
	pic_Link text,
	cname varchar,
	ename varchar,
	score numeric ,
	rated numeric ,
	instroduction text,
	info text
	)
	'''###创建数据表
	conn=sqlite3.connect(dbpath)
	cursor=conn.cursor()
	cursor.execute(sql)
	conn.commit()
	conn.close()

def main():
	baseurl="https://movie.douban.com/top250?start="
	# 爬取网页
	datalist=getData(baseurl)
	####savepath=".\\豆瓣电影Top250.xls"####
	dbpath="movie.db"
	###保存数据
	#saveData(datalist,savepath)
	saveData2DB(datalist,dbpath)
	# askURL("https://movie.douban.com/top250?start=0")
if __name__=="__main__":
	main()
	#init_db("movietest.db")
	print("保存成功")






