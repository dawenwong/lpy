# -*- codeing = utf-8 -*-
# @Time: 2021/12/23 14:22
# @Author: w
# @File:testXlwt.py
# @Software:PyCharm
import xlwt

# 创建workbook对象
workbook = xlwt.Workbook(encoding="utf-8")

# 创建一个名叫sheet1的worksheet
worksheet = workbook.add_sheet("sheet1")

# write(行,列,内容)，0行0列"cell(0,0)"写入"hello"
# worksheet.write(0, 0, "hello")
# for i in range(10):
#     for j in range(10):
#         str1 = "("+str(i)+" " + str(j)+")"
#         worksheet.write(i, j, str1)

# 9x9乘法表
# for i in range(0, 9):
#     for j in range(0, i + 1):
#         worksheet.write(i, j, "%d x %d = %d" % (i + 1, j + 1, (i + 1) * (j + 1)))
# 保存写好数据表格
workbook.save(r"C:\Users\WONG\Desktop\xlwtTest.xls")
