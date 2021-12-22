# -*- coding = utf-8 -*-
# @Time: 2021/12/21 15:37
# @Author: w
# @File:testUrllib.py
# @Software:PyCharm

import urllib.request
import urllib.parse

# get的方式请求有个网址
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response)   #返回一个 <http.client.HTTPResponse object at 0x000001A67500DC10> 对象
# print(response.read().decode('utf-8'))  # read() 得到整个网页的原代码,decode('utf-8')使用utf-8解码，整个结构更好看

# post的方式获取网址
# http://www.httpbin.org/ 这个网页可以做post测试
# data = bytes(urllib.parse.urlencoded({"name": "Kris"}), encoding="utf-8")  # bytes()将内容变成字节码
# response = urllib.request.urlopen("http://www.httpbin.org/post", data=data)
# print(response.read().decode('utf-8'))


# 访问超时处理
# try:
#     response = urllib.request.urlopen("http://www.httpbin.org/get", timeout=0.01)  #0.01秒
#     # timeout = x 秒，设置x秒，超过就处理
#     print(response.read().decode('utf-8'))  # decode('utf-8')使用utf-8字符，解析内容
# except urllib.error.URLError as e:
#     print("超时！！！")


# 响应头 header
# response = urllib.request.urlopen("http://www.baidu.com", timeout=1)
# print(response.status)  # status 状态码200就是成功，404找不到，418被发现是爬虫
# print(response.getheaders())  # 获取头部全部的内容，是一个list
# print(response.getheader("Cache-Control"))  # 获取某一个key的值


# url = "http://www.douban.com"  # 豆瓣不能直接访问，抓爬虫
# 需要伪装成浏览器去访问
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36
# 伪装成真实浏览器发送请求，不然会被检查出是爬虫

# url = "http://www.httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/96.0.4664.110 Safari/537.36 "
# }
# data = bytes(urllib.parse.urlencode({"name": "Kris"}), encoding='utf-8')
# # 封装一个req对象，包含url、header、data等信息向服务器请求
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# 伪装成浏览器访问豆瓣测试
# url = "http://www.douban.com"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/96.0.4664.110 Safari/537.36 "
# }  # "User-Agent" 就是浏览器信息
# req = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))  # 成功获取网页内容


# url = "http://192.168.1.100"
# #req = urllib.request.Request(url=url)
# response = urllib.request.urlopen(url)
# print(response.read().decode('utf-8'))