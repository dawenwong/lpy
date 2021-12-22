# BeautifulSoup4
import re

from bs4 import BeautifulSoup

file = open("./baidu.html", 'rb')  # 需要rb模式，将html文件读到内存中

# print(file.read().decode('utf-8'))

soup = BeautifulSoup(file, "html.parser")  # 将读取的html文档传入，使用html.parser解析器

# print(soup.title)  # 返回值：<title>百度一下，你就知道</title>
# print(soup.a)    # 找到第一个a标签以及a标签内的内容
# print(soup.head)  #<head>xxx</head>标签和标签内内容

# 获取标签中的内容，不要带标签
# print(soup.title.string)  # xxx.string  xxx标签中的内容

# 获取标签的attrs属性
# print(soup.a.attrs)  # 返回值字典 {'href': 'http://news.baidu.com/', 'target': 'blank'}
# print(soup.a.string)
# print(type(soup))
# print(soup)  # 整个文档

# 文档遍历
# print(soup.head.contents)   # 返回值list，每个标签及其标签中内容就是一个list中元素
# print(soup.head.contents[1])  # 取list中的索引为1的元素


# 文档搜索
# 1.通过bs提供的方法去查找
# a_list = soup.find_all("a")  # 使用bs的查找所有方法，查找a
# print(a_list)

# 2.通过使用正则表达式，使用search方法来查找内容
# a_list = soup.find_all(re.compile("a"))   # 只要包含a字母都会被找到，并且保存为一个元素
# print(a_list)

# 3.方法

# kwargs
# t_list = soup.find_all(id="head")
# t_list = soup.find_all(class_=True)  # 带class
# t_list = soup.find_all(href="https://tieba.baidu.com/index.html")
# t_list = soup.find_all(text="地图")
# t_list = soup.find_all(text=["新闻", "贴吧", "地图"])
# t_list = soup.find_all(text=re.compile("\d"))  # 包含数字

# limit 参数
# t_list = soup.find_all("a", limit=3)  # 限制只取3个
# print(t_list)

# css选择器
# print(soup.select("title"))  # 返回列表,可以是标签名/id/class查找
# print(soup.select(".left"))    # 通过类名查找，返回的是该标签包含的所有内容
# print(soup.select("#dropdown"))   # 通过id查找，返回的是该标签包含的所有内容
# print(soup.select(a[class='xxx']))
# print(soup.select("head>title"))  # head下面的title,返回值list

file.close()
