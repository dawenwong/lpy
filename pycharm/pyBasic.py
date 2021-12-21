#字典

#删除 del
#info = {"name":"Kris","age":31}
# print("删除前：%s"%info["name"])
# del info["name"]
#print("删除后: %s"%info["name"])

#clear 清空
# info = {"name":"Kris","age":31}
#del info  #删除字典
#print("删除前：%s"%info) #stack中已经没有这个变量的了
# info.clear() #.xxx()这是调用的类方法？
# print("清空后：%s"%info)  #就是个空字典
# info["age"] = 21
# print("清空后添加键值对%s"%info)


#字典查询
info = {"name":"Kris","age":31,"ID":1001}
# print(info.keys())  #获取所有的键
# print(info.values())  #获取所有的值
#print(info.items())   # 打印结果：dict_items([('name', 'Kris'), ('age', 31), ('ID', 1001)])
#for遍历字典

# for key in info.keys():
#     print(key)
# for value in info.values():
#     print(value)

# for key,value in info.items():
#     print("key = %s,value = %s"%(key,value))

#自定义[(),(),(),()]这种数据结构能不能行？
# arr = [('name','张三'),('age',15),('id',1002),('hobby','sleep')]
# for k,v in arr:  #也可以
#     print


#enumerate 枚举
# arr = ['a','b','c','d','e']
# for index,element in enumerate(arr):
#     print("index = %s,value = %s"%(index,element))
'''
打印结果:
index = 0,value = a
index = 1,value = b
index = 2,value = c
index = 3,value = d
index = 4,value = e
'''

#set集合
# s = set([1,2,3,4,2,3])
# print(s) #集合不能有重复的元素重复元素会被自动过滤，{1, 2, 3, 4}



#*********************************************************

#函数
# def greet():
#     print("你好！！！")
#
# #greet()  #调用函数


# def addNum(*agrs): #*args是一个元组
#     '''形参长度不限，返回值：输入的形参的和'''
#     sum = 0
#     for i in range(len(agrs)):
#         sum += agrs[i]
#     return sum  #函数返回值
# print(addNum(1,3,4,5,2,3,3))

# def minsNum(a,**kwargs):  #**kwargs字典形式
#     for value in kwargs.values():
#         a -= value
#     return a
# print(minsNum(1000,a1 = 100,b = 200,c = 100,d = 100))

def divide(a,b):
    shang = a//b
    yushu = a%b
    #return shang,yushu #返回值是一个tuple
    #return (shang,yushu) #返回值是一个tuple
    #return [shang,yushu]  #返回值是一个list
    return {"商":shang,"余数":yushu}  #返回值是一个dict
#print(type(divide(5,2)))

#s,y =divide(5,2) #接收元组返回值，解包
#print("商 = %s，余数 = %s"%(s,y))
#x = [x for x in divide(5,2)] #list返回值形式
#print("商 = %s，余数 = %s"%(x[0],x[1]))
# dict1 = divide(5,2)
# # print(dict1)  #字典形式
# # print(dict1.keys())
# # print(dict1.values())
# for k,v in dict1.items():
#     print("商 = %s，余数 = %s"%(k,v))






