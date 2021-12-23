# -*- codeing = utf-8 -*-
# @Time: 2021/12/23 16:14
# @Author: w
# @File:testSqlite3.py
# @Software:PyCharm
import sqlite3

# 1.打开或创建一个sqlite数据库
# 打开或创建一个sqlite数据库
# conn = sqlite3.connect("test.db")  # 可以随便命名后缀名，最好是.db,"test.db"是默认在当前路径下，也可以使用其他路径 \
# 如果当前路径下没有，test.db 就创建一个，打开或创建
# print("成功打开数据库!")


# 2.创建一张表(可以鼠标点的方式)
# conn = sqlite3.connect("test.db")  # 打开(连接)数据库
# print("成功打开数据库")
# # 获取游标（大部分数据操作步骤）
# c = conn.cursor()  # 获取游标
# # 写创建表的sql语句
# # 基本数据类型5种，NULL（null值）、INTEGER（根据值大小存储在1、2、3、4、6、8字节中）、REAL（浮点）、TEXT（字符串，utf-8编码存储）、BLOB
# sql = '''
#         create table company
#         (id int primary key not null,
#          name text not null,
#          age int not null,
#          address char(50),
#          salary real
#         );
# '''
#
# c.execute(sql)  # 执行sql语句
# conn.commit()  # 提交数据库操作，让操作生效
# conn.close()  # 断开数据库连接


# 3.插入数据
conn = sqlite3.connect("test.db")  # 连接(打开)数据库
print("成功连接数据库")
c = conn.cursor()  # 获取游标

# 写插入的sql语句
sql1 = '''
        insert into company(id,name,age,address,salary)
        values (1,"张三",39,"上海",30000)
'''
sql2 = '''
        insert into company(id,name,age,address,salary)
        values (2,"李四",20,"东莞",1500)
'''
c.execute(sql1)  # 执行sql1语句
c.execute(sql2)  # 执行sql2语句
conn.commit()  # 提交数据库操作，让操作生效
conn.close()  # 断开数据库连接
print("插入数据完毕")
