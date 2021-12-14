#-*- codeing = utf-8 -*-
#@Time :2020/8/21 22:16
#@Author: zzf
#@File : test3.0.py
#@Software: PyCharm Community Edition
#########################################函数
#########################################函数
#########################################函数

# def printinfo():
#     print ("-------------")
#     print ("人生何处不相逢")
#     print ("-------------")
# printinfo()

# def add(a,b):
#     c=a+b
#     print (c)
# add(2,8)


#####返回多个值
# def divid(a,b):
#     shang=a//b
#     yushu=a%b
#     return shang,yushu
# i,j=divid(7,3)
# print (i,j)

######局部变量
# def test1():
#     a=300
#     print ("a=%d"%a)
#     a = 500
#     print ("a=%d" % a)
#
# def test2():
#     a=100
#     print ("a=%d"%a)
#
# test1()
# test2()

######全局变量
a=100
def test1():
    global a#重新定义全局变量
    print ("a=%d" % a)
    a=500
    print ("a=%d"%a)

def test2():
    print ("a=%d"%a)

test1()
test2()


#########################################文件
#########################################文件
#########################################文件

# f=open("123.txt","w")###w有了会覆盖
# f.write("hello world0001")
# f.write("hello world0002")
# f.write("hello world0003")
# f.write("hello world0004")
# f.close()#关闭文件

#
# f=open("123.txt","r")#打开只读方式
# content=f.read(5)###读5个字符
# print (content)
# f.close()#关闭文件


# f=open("123.txt","r")#打开只读方式
# content=f.readlines()#读取整个文件
# print (content)
# m=1
# for i in content:
#     m+=1
#     print (i,end="")
#     print(m)
# f.close()#关闭文件
#
# f=open("123.txt","r")#打开只读方式
# content=f.readline()#读取一行文件
# print (content)
# f.close()#关闭文件




#########################################异常
#########################################异常
#########################################异常
# print("----------")
# f = open("1.txt", "r")####报错
# print("----------")#这句不被执行

# 捕获异常
# try:
#     print("----------")
#     f = open("1.txt", "r")
#     print("----------")
# except IOError:###文件没找到，属于IO异常
#     pass

# try:
#    print (num)
# except NameError:###异常要被捕获得一致
#     print ("产生错误了")


# try:
#     print("----------")
#     f = open("1.txt", "r")
#     print("----------")
#
#     print (num)
# except (NameError,IOError)as result:###异常都放（）里
#     print ("产生错误了")
#     print (result)

# try:
#     print("----------")
#     f = open("1.txt", "r")
#     print("----------")
#
#     print (num)
# except Exception as result:  ###Exception 所有异常父类
#     print ("产生错误了")
#     print (result)



a=(3,5)
print(type(a))
print(a[1])












