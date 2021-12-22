# 正则表达式
import re

# 创建模式对象
pat = re.compile("AA")  # 此处的AA，是创建的模版，用来校验其他字符串

m = pat.search("BCAADEAAPPLLJC")  # 结果：<re.Match object; span=(2, 4), match='AA'>
print(m)
n = pat.search("asdad")  # search()方法查找比对，找到第一个就返回
print(n)  # None 匹配不到

# 不用模式对象
a = re.search("AA", "CDFGRAADERAAQQ")   # 结果：<re.Match object; span=(5, 7), match='AA'>
print(a)

# findall("模版"，"内容"),最好加上"r"防止转义字符生效
print(re.findall("a", r"d\adeawjkjoiaxja_saxdj<sd>dsa_asdr"))  # 结果：['a', 'a', 'a', 'a', 'a', 'a', 'a']
print(re.findall("[A-Z]", r"AKlIjwCwdJaSHHXyFzbW"))  # 结果：['A', 'K', 'I', 'C', 'J', 'S', 'H', 'H', 'X', 'F', 'W']
print(re.findall("[A-Z]+", r"AKlIjwCwdJaSHHXyFzbW"))  # 结果：['AK', 'I', 'C', 'J', 'SHHX', 'F', 'W']

# sub
print(re.sub("a", "A", r"akjdaxjaora"))  # 将第三个参数中的"a"用"A" 替换，结果：AkjdAxjAorA
