# BeautifulSoup4
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
#print(soup.head.contents[1])  # 取list中的索引为1的元素


# 文档搜索


file.close()
