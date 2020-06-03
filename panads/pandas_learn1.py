import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#s = pd.Series([1,3,5,np.nan,6,8]) #添加series

#dates = pd.date_range('20130101',periods=6)#生成日期
#                  columns=list('ABCD'))
#df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

#创建一个DataFrame和excel很像，数据是random。randn随机生成，索引是前面的dates时间
#每行的标题分别是A,B,C,D，注意np。random。randn（行，列）

#df2 = pd.DataFrame({'A':1.,
                   #'B':pd.Timestamp('20190523'),
                   #'C':pd.Series(1,index = range(4),dtype='float32'),
                   #'D':pd.array([3]*4,dtype='int32'),
                   #'E':pd.Categorical(['text','train','test','train']),
                   #'F':'foo'})
#字典类型 创建数据

#print(df2.dtypes)
#print(df.tail(2))
#查看后面

#print(df.index)
#索引

#print(df.columns)
#列查看

#print(df.values)
#列表值查看

#print(df.describe())
#count 数量
#mean 平均值
#std 标准差
#min 最小值
#25% 第一四分位数 (Q1)，又称“较小四分位数”，等于该样本中所有数值由小到大排列后第25%的数字。
#50% 中位数
#75% 同上类似
#max 最大值

#print(df.T)
#转置


#print(df.sort_index(axis=0,ascending=False))
#参数axis只有两个值，分别是0和1，而df中只有两个index分别是表最左一列的时间和表最上一行
#的ABCDE
#axis=0对应的是对左边一列的index进行排序，ascending=False代表降序，ascending=True
#代表升序
#若运行sort_index(axis=0,ascending=False)后，最左边的时间列呈降序排列
#axis=1对应的是对上边一行的index进行排序，同样的，ascending=False代表降序，
#ascending=True代表升序
#若运行sort_index(axis=1,ascending=False)后，最上边的ABCDE行呈降序排列

#print(df.sort_values(by='B'))
#使用时查看详细说明

#print(df['A'])
#选择某列，产生一个series

#print(df[0:3])
#切片，选择多少行到多少行

#print(df.loc[dates[0]])
#按标签选择 ,日期的第0行个中所有的值。

#print(df.loc[:,['A','B']])
#选择列，A列和B列

#print(df.loc['20130102':'20130104',['A','B']])
#选择20130102——20130104行，A,B列的数据

#print(df.loc['20130102',['A','B']])
#只选择20130102行的A,B列的数据
 
#print(df.loc[dates[0],'A'])
#print(df.at[dates[0],'A'])
#获取第0行的A列的数字，相当有excel中第（0，A)

#print(df.iloc[3])
#选择第3行的数据

#print(df.iloc[3:5,0:2])
#3:5表示从第4行到5行的数据[3，5)，0:2表示从第0列到第1列的数据[0,2)

#print(df.iloc[[1,2,4],[0,2]])
#[1,2,4]第1,2,4行数据，0:2表示从第0列到第1列的数据[0,2)

#print(df.iloc[1:3,:])
#3:5表示从第4行到5行的数据[1，3),:表示全部的列

#print(df.iloc[:,1:3])
#全部的行，第2列和3列的数据，注意都是0开始计数

#print(df.iloc[1,1])
#print(df.iat[1,1])
#查看第1行第一列的数字

#print(df[df.A>0])
#对A行进行比较，选择出A大于0的数据

#print(df[df>0])
#从满足布尔条件的DataFrame中选择值,[df>0]输出的是bool值

#df2 = df.copy()
#copy复制df，在df2中改动不会影响df
#df2['E'] = ['one','one','two','three','four','three']
#print(df2[df2['E'].isin(['two','four'])])
#使用isin（）进行过滤


# ！！！！！！！！！！！！！！！！！
#s1 = pd.Series([1,2,3,4,5,6],
               #index=pd.date_range('20130102', periods=6))
#创建一组新的数据

#print(s1)

#df['F'] = s1
#命名为F列，数据是s1
#print(df)
#df.at[dates[0],'A'] =0
#设置操作第一种方法
#df.iat[0,1] = 0
#设置操作第二种方法
               
#df.loc[:,'D'] = np.array([5]*len(df))
#设置操作第三种方法
#print(df)

#df2 = df.copy()
#df2[df2>0] = -df2
#print(df2)

#df1 = df.reindex(index=dates[0:4], 
                 #columns=list(df.columns) + ['E'])
#df1.loc[dates[0]:dates[1],'E'] = 1
#print(df1)
#添加E列，0行到1行的数据是1

#print(df1.dropna(how='any'))
#删除缺少数据的行

#a=df1.fillna(value=5)
#print(a)
#给没有数据的位置，添加数据为5

#print(pd.isna(df1))
#取值为nan的布尔掩码。
# 115到151要整体使用！！！！！
                 
                 


#print(df.mean())
#print(df.mean(1))
#求平均数df.mean()=df.mean(0)
#0是表示列求平均数，1是行求平均数


#print(df.apply(np.cumsum))
#np.cumsum 按行累加
#将函数应用于数据：
#print(df)
#a=df.apply(lambda x: x.max() - x.min())
#print(a)
 
#s = pd.Series(np.random.randint(0, 7, size=10))
#随机生成0到6的数字，生成10个size=10。
#print(s)
#print(s.value_counts())
#s.value_counts表示计数多出现的数据
                 
#s = pd.Series(['A', 'B', 'C', 'Aaba', 
               #'Baca', np.nan, 'CABA', 'dog', 'cat'])
#创建一个字符串列
#print(s)
#print(s.str.lower())
#s.str.lower() 对字符串使用方法，lower变小写，更多方法查看手册


#df1 = pd.DataFrame(np.random.randn(10,4))
#创建一个10行4列的dataframe
#print(df1)
#pieces = [df1[:3], df1[3:7]]
#对df1进行切片
#print(pieces)
#print(pd.concat(pieces))
#将切的片数据连接起来
               
#left = pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})
#right= pd.DataFrame({'key':['foo','foo'],'rval':[4,5]})

#print(pd.merge(left,right,on='key'))
#将两个dataframe合并
               
#df1 = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
#print(df1)
#s = df1.iloc[3]
#查找第三行的值
#print(s)
#a = df1.append(s, ignore_index=True)
#将第三行添加到df1中
#print(a)

#df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
                  # 'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
                  # 'C' : np.random.randn(8),
                  # 'D' : np.random.randn(8)})

#print(df)
#print(df.groupby('A').sum())
#A 按foo行和bar行分类，把foo行的值相加，
#B 按one three two行分类
                  
#print(df.groupby(['A','B']).sum())
#按照下面的结果分类相加，
#bar one    0.702272  0.711211
    #three -0.652974 -0.654270
    #two   -0.114540  1.389388
#foo one   -0.884227 -0.761495
    #three -0.173322  0.540028
    #two   -0.740912 -1.783281
    
#df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                 #  'B' : ['A', 'B', 'C'] * 4,
                 #  'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                  # 'D' : np.random.randn(12),
                 #  'E' : np.random.randn(12)})

#print(df)
#r = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
#print(r)
                 
#数据透视表，如下
#C             bar       foo
#A     B                    
#one   A -0.555514 -0.627641
      #B  1.982875 -0.741491
     # C -0.278647  0.680479
#three A -1.220103       NaN
     # B       NaN  0.702644
     # C  1.274008       NaN
#two   A       NaN  0.914110
     # B  0.720528       NaN
     # C       NaN  1.232269
     
     
 # a= df.to_csv('foo.csv')
 #写入csv数据
 # b=df.to_csv('foo.csv')
 #读取CSV数据
 
 #a=df.to_excel('foo.xlsx', sheet_name='Sheet1')
 #写入excel数据
 #pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])














