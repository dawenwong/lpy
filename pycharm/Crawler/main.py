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
        response = urllib.request.urlopen(request)  # 请求获取网页对象
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 创建正则模板
link_pat = re.compile(r'<a href="(.*?)">')  # 找到a标签链接
imgSrc_pat = re.compile(r'<img.*src="(.*?)"', re.S)  # 找到img标签，图片的；链接，re.S忽略换行，包含换行符在里面
name_pat = re.compile(r'<span class="title">(.*)</span>')  # 找到影片的名字
rating_pat = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 影片的评分
judge_pat = re.compile(r'<span>(\d*)人评价</span>')  # 找到评价人数
inq_pat = re.compile(r'<span class="inq">(.*)</span>')  # 找到评价内容
bd_pat = re.compile(r'<p class="">(.*?)</p>', re.S)  # 找到影片相关内容，导演等,re.S忽略换行，包含换行符在里面


# 爬取网页
def getData(baseUrl):
    """获取网页的数据列表"""
    dataList = []
    for i in range(0, 1):
        url = baseUrl + str(i * 25)  # https://movie.douban.com/top250?start=25,每页网页是25部电影
        html = askUrl(url)
        # 逐一解析网页数据
        soup = BeautifulSoup(html, "html.parser")
        # print(soup)
        # i = 1
        for item in soup.find_all("div", class_="item"):  # 找到每个calssName是item的div
            # print(item)
            data = []
            item = str(item)  # 不强制转换为string 会报错
            linkList = re.findall(link_pat, item)[0]  # 取返回列表中的第一个元素，因为网页中有2个相似的a标签，防止重复
            data.append(linkList)  # 将找到的链接添加到列表
            # print("%d : %s" % (i, linkList))
            # i += 1
            imgSrc = re.findall(imgSrc_pat, item)[0]  # 取返回列表中的第一个imgsrc
            data.append(imgSrc)  # 将找到的图片链接添加到列表
            name = re.findall(name_pat, item)  # 这里因为有的电影有中文和外文名，有的没有，需要做判断分情况存放
            if len(name) == 2:  # 返回值列表的长度大于2，说明有有中文和外文名
                chinese_name = name[0]  # 获取列表中索引0的中文名字
                data.append(chinese_name)  # 添加中文名字到列表
                foreign_name = name[1].replace("/", "")  # 获取列表中索引1的外文名字,因为外文名中有“/”，使用replace将其替换为空
                data.append(foreign_name)  # 添加外文名字到列表
            else:  # 其他情况只有1个名字
                chinese_name = name[0]  # 获取列表中索引0的中文名字
                data.append(chinese_name)  # 添加中文名字到列表
                foreign_name = " "  # 虽然没有外文名字，但也不能不添加，自定义外文名为空，方便后面保存等操作
                data.append(foreign_name)  # 添加空的外文名字到列表
            rate = re.findall(rating_pat, item)[0]  # 查找影片评分
            data.append(rate)  # 添加影片评分到data列表
            judgeNum = re.findall(judge_pat, item)[0]  # 查找评价人数,[0]取出值
            data.append(judgeNum)  # 添加评价人数到data列表
            inqContent = re.findall(inq_pat, item)  # 查找影片评价内容
            # 这里和影片名字一样，有些影片可能有也可能没有，因此要分情况添加
            if len(inqContent) != 0:  # 非0，影片有评价内容
                inq = inqContent[0].replace("。", "")  # 去掉“。”
                data.append(inq)  # 添加评价内容到data列表
            else:  # 没有评价内容
                # inqContent = " "  # 没有评价内容，就定义一个空字符，占位，方便后面的操作
                data.append(" ")  # 添加空评价内容到data列表
            bd = re.findall(bd_pat, item)[0]  # 查找导演主演等信息
            # bd内容中有"<br> /"等符号，这是需要去掉的
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # \s空格，sub(pat,replace,str)将str中的pat替换为replace
            bd = re.sub('/', " ", bd)  # 去掉 ’/‘
            data.append(bd.strip())  # 去掉空格，添加到data列表

            dataList.append(data)  # 将一部电影的信息，放入dataList中
    # print(dataList)
    return dataList


# 保存获得的数据
def saveData(savePath):
    """保存数据，位置：savaPath"""


if __name__ == "__main__":  # 感觉相当于int main(){ }或public static void main(String[] args){}
    # #main()          #作为整个程序的入口
    # askUrl("https://movie.douban.com/top250?start=")
    # getData("https://movie.douban.com/top250?start=")
   print(" ")