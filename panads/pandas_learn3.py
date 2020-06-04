"""Essential basic functionality"""
import pandas as pd
import numpy as np 
# index = pd.date_range('1/1/2000',periods=8)
# # print(index)
# s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
# print(s)
# df =pd.DataFrame(np.random.randn(8,3),index=index,columns=['A','B','C'])

"""Head and tail"""
# #To view a small sample of a series or dataframe object,use the "head()" and "tail()"method.The default number of 
# #elements to display is five,but you may pass a custom number 
long_series = pd.Series(np.random.randn(1000))
print(long_series.head())
print(long_series.tail())