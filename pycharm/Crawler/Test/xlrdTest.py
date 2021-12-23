# -*- codeing = utf-8 -*-
# @Time: 2021/12/23 14:47
# @Author: w
# @File:xlrdTest.py
# @Software:PyCharm
import xlrd

# 打开excel文件创建'xlrd.book.Book'对象
wb = xlrd.open_workbook(r"C:\Users\WONG\Desktop\xlrdTest.xls")
# print(type(wb))
# 获取所有sheet名
sheet_names = wb.sheet_names()
# print(sheet_names)  # 结果：['sheet1', 'Sheet2', 'Sheet3', 'Sheet4', 'Sheet5', 'Sheet6'] 列表
# print(sheet_names[1])  # 结果： Sheet2

# sheet_by_index(1)，通过索引号，
# sheet2 = wb.sheet_by_index(1)  # sheet2
# print("sheet2名称：%s \nsheet2行数：%d \nsheet2列数：%d" % (sheet2.name, sheet2.nrows, sheet2.ncols))
# sheet2名称：Sheet2
# sheet2行数：9
# sheet2列数：4

# sheet_by_name("sheet2")  通过sheet名字查找
# sheet2 = wb.sheet_by_name("Sheet2")
# print("sheet2 name: %s\nsheet2 rows: %d\nsheet2 cols: %d"%(sheet2.name, sheet2.nrows, sheet2.ncols))
# sheet2 name: Sheet2
# sheet2 rows: 9
# sheet2 cols: 4

# 获取整行或整列的值
sheet1 = wb.sheet_by_name("sheet1")
# print(sheet1.row_values(2))  # 获取第3行的所有值
# print("**********************************************")
# print(sheet1.col_values(2))  # 获取第3列的所有值

# 获取指定单元格的内容
# print(sheet1.cell(0, 0).value)  # 获取第1行第1列的，单元格的值
# print(sheet1.cell_value(0, 0))  # 获取第1行第1列的，单元格的值
# print(sheet1.row(0)[0].value)  # 获取第1行第1列的，单元格的值

# 获取单元格内容的数据类型
# print(sheet1.cell(1, 1).ctype)
# print(sheet1.cell(1, 1))  # 直接打印结果：number:31.557464844636396
# 说明：ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error



