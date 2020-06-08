"""Essential basic functionality"""
import pandas as pd
import numpy as np 
# index = pd.date_range('1/1/2000',periods=8)
# # print(index)
# s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
# # print(s)
# df =pd.DataFrame(np.random.randn(8,3),index=index,columns=['A','B','C'])

"""Head and tail"""
# #To view a small sample of a series or dataframe object,use the "head()" and "tail()"method.The default number of 
# #elements to display is five,but you may pass a custom number 
# long_series = pd.Series(np.random.randn(1000))
# print(long_series.head())
# print(long_series.tail())

"""Attributes and underlying data"""
# #pandas object have a number of attributes enabling you to access the metadata.
   # #"shape":give the axis dimensions of the object,consistent with ndarry.
   # #"Axis labels": 1.series :index (only axis)
   # #               2.DataFrame:index(rows) and columns
# print(df[:2])
# df.columns = [x.lower() for x in df.columns]
# print(df)
# #Pandas objects (Index,Series,DataFrame) can be thought of as container of arrays,which hold the actual 
# #data and do the actual computation.For many types,the underlying array is a numpy.ndarray.however,pandas 
# #and 3rd party libraries may extendNumpy's type system to add support for custom arrays.
# #To get the actual data inside a Index or Series,use the .array property
# print(s.array)
# print(s.index.array)
# #if you know you need a numpy array,use "to_numpy()" or numpy.asarray().
# print(s.to_numpy())
# print(np.array(s))
# #If a DataFrame contain homogeneously-typed data,the ndarry can actually be modified in-place,and the changes 
# #will be reflected in the data structure.The hetergeneous data(e.g. some of the DataFrame's column are not 
# #all the same dtype),this will not be the case.The values attribute itself,unlike the axis labels,cannot be 
# #assigned to.
# #note:When working with hetergeneous data,the dtype of the resulting ndarray will be chosen to accommodate all
# #of the data involved.For example,if strings are involved ,the result will be of object dtype.If there are only
# #floats and integers,the results array will be of float dtype.
# #In the past,pandas recommended Series.values or DataFrame.values for extracting  data from a Series or DataFrame,
# #You'll still find references to these in old code bases and online.Going forward,we recommend avoiding ".values"
# #and using ".array"or ".to_numpy()". ".values"has the following drawbacks:

"""Flexible binary operations"""
# #With binary operations between pandas data structures,there are two key points of interest:
   # #Broadcasting behaivor between higher -(e.g. DataFrame) and lower dimensional(e.g. Series) objects
   # #Missing data in computations.

# #Matching /broadcasting behaivor
# #DataFrame has the methods add(),sub() ,mul(),div() and related functions radd(),rsub(),...for carrying out 
# #binary opetations.For broadcasting behavior,Series input is of primary interest.Using these functions,you can 
# #use either match on index or column via the axis keyword.
# df = pd.DataFrame({
#    'one':pd.Series(np.random.randn(3),index=['a','b','c']),
#    'two':pd.Series(np.random.randn(4),index=['a','b','c','d']),
#    'three':pd.Series(np.random.randn(3),index=['b','c','d'])})
# print(df)
# row = df.iloc[1]
# print(row)
# column =df['two'] 
# print(column)
# print(df.sub(row,axis='columns'))
# print(df.sub(column,axis='index'))
# print(df.sub(column,axis=0))
# #Futhermore you can  align a level of a Multilndexed DataFrame with a Series.
# dfmi = df.copy()
# print(dfmi)
# dfmi.index = pd.MultiIndex.from_tuples([(1,'a'),(1,'b'),(1,'c'),(2,'a')],names=['first','second'])
# print(dfmi)
# print(dfmi.sub(column,axis=0,level='second'))
