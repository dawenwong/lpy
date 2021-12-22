# -*- coding = utf-8 -*-
# @Time: 2021/12/21 11:13
# @Author: w
# @File:main.py
# @Software:PyCharm

import urllib.request, urllib.error  # 指定url，获取网页数据
from bs4 import BeautifulSoup  # 对网页解析，获取数据
import re  # 正则
import urllib.request, urllib.error  # 指定url，获取网页数据
import xlwt  # 对excel进行操作
import sqlite3  # 对sqlite数据库进行操作的
import ssl

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context


def main():
    baseUrl = "https://movie.douban.com/top250?start="  # 要被爬取数据的基础网址
    # 1.爬取网页
    dataList = getData(baseUrl)

    # 2.对网页逐一解析，获得数据

    # 3.保存数据
    savePath = r".\豆瓣电影TOP250.xls"  # 当前路径,创建一个excel文件
    saveData(savePath)


# 爬取网页
def getData(baseUrl):
    """获取网页的数据列表"""
    dataList = []
    for i in range(0, 10):
        url = baseUrl + str(i * 25)  # https://movie.douban.com/top250?start=25,没页网页是25部电影
        html = askUrl(url)
        # 逐一解析网页数据

    return dataList


# 得到一个指定网页的内容
def askUrl(url):
    """返回string类型 ，单个网页的内容"""
    head = {  # 模拟头部伪装，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                      "Chrome/96.0.4664.110 Safari/537.36 "
    }
    # head User-Agent 用户代理是用来告诉被访问的服务器
    request = urllib.request.Request(url, headers=head)  # 创建对象
    html = ""  # 存储网页
    # 异常处理
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存获得的数据
def saveData(savePath):
    """保存数据，位置：savaPath"""


if __name__ == "__main__":  # 感觉相当于int main(){ }或public static void main(String[] args){}
    # #main()          #作为整个程序的入口
    askUrl("https://movie.douban.com/top250?start=")
