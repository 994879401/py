#-*- codeing = utf-8 -*-
#@Time :2020/8/8 9:56
#@Author: zzf
#@File : test2.0.py
#@Software: PyCharm Community Edition

#
#########################################元组
#########################################元组
#########################################元组
# tup1=()#创建空元组
# print (type(tup1))
#
# tup2=(50)#加50整型
# print (type(tup2))
#
# tup3=(50,)
# print (type(tup3))
#
# tup4=("abc","def",200,300)
# print (type(tup4))
# print (tup4[0])
# print (tup4[-1])
# print (tup4[1:5])

################################增
# tup1=(12,34,56)
# print (type(tup1))
# tup2=("abc","def")
# tup=tup1+tup2
# print (tup)
#
# ################################删
# # tup1=(12,34,56)
# # print (tup1)
# # del tup1
# # print ("已删除tup1")
# # print (tup1)###报错
#
# ################################不能改
# ##不能改
#
#
# ################################查
# tup1=(12,34,56)
# print (tup1[1])


# #########################################字典
# #########################################字典
# #########################################字典
# dict={"name":"吴彦祖","age":18}
# print (dict["name"])
# print (dict["age"])
#
# # ###访问不存在键
# # print (dict["sex"])###不存在报错
# print (dict.get("sex"))##使用Get()方法，没有返回None
# print (dict.get("sex","m"))##使用Get()方法，没有返回默认值，这里没有返回m
#
# ##################################增
dict={"name":"吴彦祖","age":18}
newID=input("输入newID")
m=input("输入v:")
dict[m]=newID
print (dict)



# # ################################删
# info={"name":"吴彦祖","age":18}
# print ("删除前：%s"%info)
# del info#####删除info
# print ("删除后：%s"%info)##报错

info={"name":"吴彦祖","age":18}
print (info)
del info["name"]###删除键值对
print (info)


info={"name":"吴彦祖","age":18}
print ("清空前：%s"%info)
info.clear()
print ("清空后：%s"%info)


################################改
info={"name":"吴彦祖","age":18}
print ("修改前：%s"%info)
info["age"]=20
print ("修改后：%s"%info)

# ################################查
#
# info={"ID":1,"name":"吴彦祖","age":18}
# print (info.keys())###得到所有的键(列表)
#
# print (info.values())###得到所有的值(列表)
#
# print (info.items())###得到所有的键值对(列表)，键值对是元祖

##遍历
# for key,value in info.items():
#     print ("key=%s,value=%s"%(key,value))

#####使用枚举
# list=["a","b","c","d"]
# print (enumerate(list))
# for i,x in enumerate(list):###枚举
#     print (i,x)


#########################################集合
#########################################集合
#########################################集合
# s=set([1,2,3])
# print (s)
# s=set([1,1,2,2,3,4])
# print (s)