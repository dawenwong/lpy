########################################################################################
"""step1  is import it"""
# #  "# #"is note 
# # "#" is code 
######################################################################################
#import pandas as pd

# df = pd.DataFrame({
#     "Name":["Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth"],
#     "Age":[22,34,25],
#     "Sex":["male","male",'female']}
#     )
#print(df)

#print(type(df["Age"])) ##elect the "Age" column
##class 'pandas.core.series.Series'
##the result is a pandas Series

##create a Series
#ages = pd.Series([22,23,18],name='Age')
# print(ages)


#求Series最大和最小
# print(df["Age"].max())
# print(ages.min())


#print(df.describe())
# #              Age
# # count   3.000000
# # mean   27.000000
# # std     6.244998
# # min    22.000000
# # 25%    23.500000
# # 50%    25.000000
# # 75%    29.500000
# # max    34.000000
# #the describe() method provides a quick overview of 
# #the numerical data in a dataframe and return a pandas Serires
##################################################################################################
"""step 2 How do I read and write tabular data?"""
###################################################################################################
#如何读写数据
#import pandas as pd

#titanic = pd.read_csv('titanic.csv')
# #pandas provides the read_csv() function to read data stored
# #as a csv file into a pandas dataframe.
# # many different file formats or data 
# # sources out of the box (csv, excel, sql, json, parquet, …),
# # each of them with the prefix read_*. 

#print(titanic.head(8))
# #to see the first 8 rows of a pandas DataFrame
# #but if you interested in the last N rows of a pandas DataFrame
# #there is also provides a tail() method,like head()

# #a check on each of the column data types by requesting the pandas dtypes
#print(titanic.dtype)
# #notes:when asking for the dtypes,no brackets() are used.
# #dtypes is an attribute of a DateFrame and Series,not a method,so no brackets

# #requset a data as a spreadsheet
#titanic.to_excel("titanic.xlsx",sheet_name='passengers',index=False)
# #whereas read_(csv,excel,json,SQL...) functions are used to read data to pandas
# #the to_(csv,excel,json,SQL...) methods are used to stored data
# #the sheet_name = '****' instead of the default sheet1
# #by setting the index = False the row index labels are not saved in the spreadsheet.
#titanic=read_excel("titanic.xlsx",sheet_name='passengers')

#################################################################################################
"""step3 How do I select a subset of a DataFrame"""
"""如何选择子集列或者行"""
##################################################################################################
#import pandas as pd

#titanic = pd.read_csv(r"data\titanic.csv")
# print(titanic.head(8))
# print(titanic.tail())
#print(titanic.info())
# print(titanic.describe())
# print(titanic.dtype)

#ages = titanic['Age']
#print(ages.head())
# #to select a single column,use square brackets[]
# #with the column name
# #each column in dataframe is a series 

#print(ages.shape)
# #look at the shape of the series
# # by use .shape
# #DataFrame.shape is an attribute,so there is no brackets.
# #a pandas is 1-dimensional and only the number of rows is returned

#age_sex = titanic[['Age','Sex']]
# print(age_sex.head())
# print(age_sex.shape)
# #to select multiple columns,use a list of columns names within 
# #the selection brakets[]

""" how do i filter specific rows from a dataframe?"""
"""如何过滤特殊信息的行"""
#eg.I'm interested in the passengers older than 35 years
#above_35 = titanic[titanic["Age"] > 35]
# print(above_35.head(10))
# print(titanic['Age']>35)
# #it will print True or False
# #only rows for which the value is true will be selected
#print(above_35.shape)
# #checking the shape attribute
# #the original titanic dataframe consists of 891 rows,but now which
# satisfy the condition (217, 12)
#print(titanic.head())

# #the passengers from cabin class 2 and 3
# class_23 = titanic[titanic["Pclass"].isin([2,3])]
# print(class_23.head())
# # the isin()conditional function return a True for each row the values
# # in the provides list.
# #the above is equivalent to filtering by rows for which the class is either 2 or 3
# #and combining the two statement with an |(or) operator:
# class_23 =titanic[(titanic['Pclass']==2) | (titanic['Pclass']==3)]
# print(class_23)
# #note:when combining multilple conditional statements,each condition must be surrounded by
# #parentheses(),moreover,you can use or/and but need to use the or operator | and the and operator &

# #the notna() conditional function
#age_no_na = titanic[titanic["Age"].notna()]
#print(age_no_na)
# #The notna() conditional function return a True for each row the values are not an Null value.    
# #you might wonder what actually changed,as the first 5lines are still the same values. 
# #One way to verify is to check if the shape has changed.
#print(age_no_na.shape) # #yeah!it changed. 

""" how do i select specific rows and columns from a dataframe?"""
# adult_names = titanic.loc[titanic["Age"]>35,"Name"]
# print(adult_names)
# #in this case,a subset of both rows and columns is made in one go,
# #just using selection brakets[] is not sufficient anymore. 
# #the loc/iloc operators are required in front of the selection braket[],
# #when use loc/iloc,the part before the comma is the rows you want,and the part after the comma
# #is the columns you want to select. 
# #for both the part before and after the comma,you can use a single label,a list of labels,
# #a slice of labels,a conditional expression or a colon.using a colon specificies you want to select 
# #all rows and column. 

# #interested in rows 10 till 25 and columns 2 to 5. 
#print(titanic.iloc[10:25,2:5])
# #when specifically interested in certain rows and/or column based on their position in the table,
# #use the iloc opetator. 

# # new value can be assigned to the selected data.For example,to assign the name "anonymous"
# # to the first three elements of the third column.
#titanic.iloc[0:3,3] = "anonymous"
#print(titanic.head(8))
"""remember:
        When selecting subsets of data,square brackets [] are used. 
        Inside these brackets,you can use a single row/column label,a list of row/column labels,
        a slice of labels,a conditional expression or a colon.  
        Select specific row/column using "loc" when using the row and column names. 
        Select specific rows and/or columns using "iloc" when use the position in the table. 
        You can assign new values to a selection based on "loc/iloc". 
"""

#################################################################################################################
"""step 4 How to create plot in pandas?"""

#################################################################################################################
# import pandas as pd
# import matplotlib.pyplot as plt 


# air_quality = pd.read_csv(r"data\air_quality_no2.csv",
#                             index_col=0,parse_dates=True)
# #note:The usage of the index_col and parse_dates parameters of the read_csv funtion 
# # to define the first(0th) column as index of the resulting dataframe
# # covnert the dates in the column to Timestamp objects,respectively. 


# #quickly visual check of the data.
#print(air_quality.head())
# air_quality.plot()
# plt.show() # # if you add the plt.show() method,you can't see the figure of the data. 
           # #don't forget this statement,it'e very important!

# # ploting only the columns of the data table with the data from Paris
#air_quality["station_paris"].plot()
#plt.show()
# #hence,the plot() method works on both Series and DataFrame

# #To visually compare the NO2 values measured in London versus Paris. 
# air_quality.plot.scatter(x = "station_london",
#                          y = "station_paris",
#                          alpha = 0.5)
# plt.show()                        
# #apart from the default line plot when using the plot function,
# #a number of alternatives are available to plot data. 

"""Using some standard Python to get an overview of the available plot method"""
# x = [method_name for method_name in dir(air_quality.plot)
#                    if not method_name.startswith("_")]
# print(x)
# #['area', 'bar', 'barh', 'box', 'density', 
# #'hexbin', 'hist', 'kde', 'line', 'pie', 'scatter']
# #one of the options is DataFrame.plot.box(),which refers to a boxplot,
# #the boxplot,for example:
# air_quality.plot.box()
# plt.show()

# #each of the column in a separate subplot
# axs = air_quality.plot.area(figsize=(12,4),subplots=True)
# plt.show()

# fig , axs = plot.subplots(figsize=(12,3)) # #create an empty matplotlib figure an axes
# air_quality.plot.area(ax = axs)  # #use pandas to put the area plot on the prepared figure/axes
# axs.set_ylable("NO$_2$ concentration") # #Do any matplotlib customization you like
# fig.savefig("no2_concentrations.png") #save the fig using the existing matplotlib method

#####################################################################################################################
"""step5 how to create new columns derived from existing columns?"""

#######################################################################################################################
# import pandas as pd 

# air_quality = pd.read_csv(r"data\air_quality_no2.csv",
#                           index_col=0,parse_dates=True)

#print(air_quality.head())
# # if we want to express the NO2 concentration of the station in London in mg/m3
# #if we assume the temperature of 25 Celsius and the pressure of 1033hPa,the conversion factor is 1.882
# air_quality['london_mg_per_cubic'] = air_quality['station_london']*1.882
# print(air_quality.head())
# #To create a new column,use []brackets with the new column name at the left side of the assignment
# #note:The calcultion of the values is done element_wise,This mean all values in the given column are 
# #multipled by the value 1.882 at once.You do not need to use loop to iterate each of the rows!

# #check the ratio of the values in paris versus antwerp and save the result in new column. 
# air_quality['ratio_paris_antwerp'] = \
#                             air_quality['station_paris'] / air_quality['station_antwerp']
# print(air_quality.head())
# #The calculation is again element-wise,so the / applied for the values in each rows
# #also other mathematical operators (+-*/) or logic operators(<,>,=...) work element-wise,

# # rename the data columns to the corresponding station identifiers
# air_quality_renamed = air_quality.rename(
#          columns={"station_antwerp":"BETR801",
#                   "station_paris":"FR04014",
#                   "station_london":"London Westminster"})

#print(air_quality_renamed.head())
# #The rename() function can be used for both row labels and column labels,provide a dictionary with the key 
# #the current names and the values the new names to update the corresponding names. 

# #mapping function as well
# air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
# print(air_quality_renamed.head())


###################################################################################################################
"""step 6 how to calculate summary statistics?"""

###################################################################################################################
# import pandas as pd 

# titanic = pd.read_csv("data\\titanic.csv")
#print(titanic.head())

""" Aggregrating statistics"""
# #the average age of the titanic passengers
#print(titanic['Age'].mean())
# # the median age and ticket fare price of the titanic passengers
#print(titanic[['Age','Fare']].median())
# #The statistic applied to multiple columns of the dataframe
#print(titanic[['Age','Fare']].describe())
# #the aggregrating statistic can be calculated for multiple colunmns at the same time.  

# # Instead of the predefined statistics,specific combinations of aggregrating statistics for given 
# #columns can be defined using the DataFrame.agg() method:
# titanic_agg = titanic.agg({
#             'Age':['min','max','median','skew'],
#             'Fare':['min','max','median','mean']})
# print(titanic_agg)

""" aggregrating statistic grouped by category"""
# #the average age for male versus female titanic passengers
#print(titanic[['Sex','Age']].groupby('Sex').mean())
# #as our interested in the average age  for each gender,a subselection on these two column
# #is made first.Next,the groupby()method is applied on the Sex column to make a group per 
# #category.The average age for each gender is calculated and return. 

# # In the previous example,we explicitly selected the 2 columns first,if not,the mean() method
# #is applied to each column containing numerical column. 
#print(titanic.groupby('Sex').mean())
# #It does not make much sense to get the average value of the Pclass.

# #if we only interested in the average age for each gender,the selection of 
# #columns is supported on the grouped data as well:
#print(titanic.groupby('Sex')['Age'].mean())

# # the mean ticket fare price for each of the sex and cabin class combinations
#print(titanic.groupby(['Sex','Pclass'])['Fare'].mean())
# #Groping can be done bu multiple columns at the same time,provides the column name at the list of 
# #dataframe.

"""count number of records by category"""
# #the number of passengers in each of the cabin classes
#print(titanic['Pclass'].value_counts())
# #The value_counts()method counts the number of records for each category in a column
# #The fucntion is a shortcut,as it is actually a groupby operation in combination with counting of the 
# #number of records within each group
#print(titanic.groupby('Pclass')['Pclass'].count())


##################################################################################################################
"""step 7 hou to reshape the layout of table"""

###################################################################################################################
# import pandas as pd
# import matplotlib.pyplot as plt 

# titanic = pd.read_csv('data\\titanic.csv')
# #print(titanic.head())

# air_quality = pd.read_csv(r"data\air_quality_long.csv",
#                         index_col="date.utc",parse_dates=True)
# print(air_quality.head())
# #sorting the titanic data according to the age of the passenger 
#print(titanic.sort_values(by='Age').head())

# #sorting the titanic data according to the Cabin class and the age in descending order
#print(titanic.sort_values(by=['Pclass','Age'],ascending=False).head())
# #with Series.sort_values().the rows in the table are sorted according to the defined column,
# #The index will follow the row order

# #long to wide table format
# #let's use a small subset of the air quality data set. 
# #we focus on the NO2 data and only use the first two measurement of each location. 
# #filter for NO2 data only
#print(air_quality.head())
#print(air_quality.tail())
# no2 = air_quality[air_quality['parameter']=='no2']
# pm25 = air_quality[air_quality['parameter']=='pm25']
# #use 2measurements (head) for each location (groupby)
# no2_subset = no2.sort_index().groupby(['location']).head(2)
# pm25_subset = pm25.sort_index().groupby(['location']).head(2)
#print(no2_subset)
# #The values for the three station as separate columns next to each other
#print(no2_subset.pivot(columns='location',values='value'))
# #The pivot()function is purely reshaping the data:a single value of each index/column
# #combination is required

#print(no2.head())
#no2.pivot(columns='location',values='value').plot()
# pm25.pivot(columns='location',values='value').plot()
# plt.show()

# #pivot table
# #i want the mean concerntrations for NO2 and PM2.5 in each stations in table form
# x = air_quality.pivot_table(values='value',index='location',
#                             columns='parameter',aggfunc="mean")
#print(x)   
# #In the case of pivot(),the data is only rearranged.When multiple values need to aggregrated
# #(In this specific case,the values on different time steps)pivot_table() can be used. providing
# #an aggregation function(e.g. mean) on how to combine these values
# #pivot table is a well known concept in spreadsheet software.when interested in summary columns for 
# #each variable separately as well,put the margins parameter to true.
# x = air_quality.pivot_table(values='value',index='location',
#                             columns='parameter',aggfunc="mean",margins=True)
# print(x)                
# #if case you are wondering,pivot_table() is indeed directly linked to groupby(),
# #The same result can be derived by grouping on both parmeter and location
# x = air_quality.groupby(['parameter','location']).mean()
# print(x)

# #wide to long format
# no2 = air_quality[air_quality['parameter']=="no2"]
# no2_pivoted = no2.pivot(columns='location',values='value').reset_index()
# #using the reset_index()function  add a new index to the data
#print(no2_pivoted)

# #collecting all air quality NO2 measurements in a single column(long format)
# no_2 = no2_pivoted.melt(id_vars='date.utc')
# print(no_2)
# #the pandas.melt()method on a dataframe converts the date from wide format to long format.
# #The column headers become the variable names in the newly created coloumn
# #The method will melt all column not mentioned in id_vars together into two columns. 
# #the pandas.melt() can be defined in more detail:
# no_2 = no2_pivoted.melt(id_vars='date.utc',
#                         value_vars=["BETR801",
#                                     "FR04014",
#                                     "London Westminster"],
#                         value_name='NO_2',
#                         var_name='id_location')
# print(no_2)        


######################################################################################################################

"""step 8 How to combine data from multiple table"""
#######################################################################################################################
# import pandas as pd

# air_quality_no2 = pd.read_csv(r'data\air_quality_no2_long.csv',parse_dates=True)
# #print(air_quality_no2)
# air_quality_no2 = air_quality_no2[['date.utc','location','parameter','value']]
# #print(air_quality_no2)
# air_quality_pm25 = pd.read_csv(r'data\air_quality_pm25_long.csv',parse_dates=True)
# air_quality_pm25 = air_quality_pm25[['date.utc','location','parameter','value']]
#print(air_quality_pm25)

# #combine the measurements of NO2 and PM2.5,two tables with a similar structure,
# #in a singlr table 
# air_quality = pd.concat([air_quality_pm25,air_quality_no2],axis=0)
#print(air_quality)
# #The concat() function performs concatenation operations of multiple tables along one of 
# #the axis(row-wise or column-wise),by default concatenation is along axis 0,so the resulting 
# #table  combines the rows of the input tables
# print('Shape of the `air_quality_pm25` table: ', air_quality_pm25.shape)
# print('Shape of the `air_quality_no2` table: ', air_quality_no2.shape)
# print('Shape of the `air_quality` table: ', air_quality.shape)
# #The axis argument will return in a number of pandas methods that can be applied
# #along an axis.a dataframe has two corrsesponding axes. 
# print(air_quality.sort_values('date.utc').head())


# #In this specific example,the parameter column provided by the data ensure that
# #each of the orginal can be indentified. But this is not always the case.the concat
# #function provides a convenient solution with the keys argument,add an additional row index
# air_quality = pd.concat([air_quality_pm25,air_quality_no2],
#                         keys=['PM2.5','NO2'])
# print(air_quality)

# #Join tables using common identifier
# #Using the merge()function ,for each of the rows in the air_quality table.the corresponding 
# #coordinates are added from the air_quality_stations_coor table.
# air_quality = pd.merge(air_quality,air_quality_parameter,
#                        how='left',on='location')
# #check the 'location' of the two tables
# air_quality = pd.merge(air_quality,air_quality_parameter,
#                        how='left',left_on='parameter',right_on='id')

# #means:left_on='parameter' == ringht_on='id'



#############################################################################################################
"""step 9 :How to handle time series data with ease?"""

##############################################################################################################
import pandas as pd 
import matplotlib.pyplot as plt 
air_quality = pd.read_csv(r'data\air_quality_no2_long.csv')
air_quality = air_quality.rename(columns={'date.utc':'datetime'})

# print(air_quality.city.unique())

# #Using  pandas datetime properties
# #I want to work with the dates in the column datetimes as datetime objects instead of  plain text
air_quality['datetime'] = pd.to_datetime(air_quality['datetime'])
#print(air_quality['datetime'])
# #Initially,the values in 'datetime' are character strings and do not provide any datetime operations.
# #By applying the 'to_datetime' function,pandas interprets the strings and convert these to datetime 
# #objects.In pandas we call these datetime objects similar to 'datetime.datetime' from standard library
# #a 'pandas.Timestamp'.

# #What is the start and the end date of the time series data set working with?
# print(air_quality['datetime'].min(),air_quality['datetime'].max())
# #Using 'pandas.Timestamp' for datetimes enable us to calculate with date information and make them
# #comparable.Hence,we can use this to get the length of our time series.
# time_duration = air_quality['datetime'].max()-air_quality['datetime'].min()
# print(time_duration)

# #add a new column to the DataFrame containing only the month of the measurement
# air_quality['month'] = air_quality['datetime'].dt.month
# print(air_quality.head())
# #By using 'Timestamp' objects for dates,a lot of time-related properties are provided by pandas.
# #All of these properties are accessible by the 'dt' accessor. 

# #the average NO2 concentration for each day of the week for each of the measurement locations?
# x=air_quality.groupby([air_quality['datetime'].dt.weekday,'location'])['value'].mean()
# print(x)
# #Here we want to calculate a given statistic(e.g. mean NO2)for each weekday and for each measurement
# #location.To group on weekdays,we use the datetime property 'weekday'(with Mondat=0 and Sunday=6) 
# #of pandas 'Timestamp',which is also accessble by the 'dt' accessor.The grouping on both locations
# #and weekdays can be done to split the calculation of the mean on each of the measurement.

# #Plot the typical NO2 pattern during the day of our time series of all station together.In other words,
# #what is the average value for each hour of the day?
# fig,axs=plt.subplots(figsize=(12,4))
# air_quality.groupby(air_quality['datetime'].dt.hour)['value'].mean().plot(kind='bar',
#                                                                           rot=0,
#                                                                           ax=axs)
# plt.xlabel('Hour of the day')
# plt.ylabel('$NO_2(μg/m^3)$')
# plt.show()                                                                
# #Similar to the previous case,we want to calculate a given statistic for each hour of the day,and we can 
# #use the split-apply-combine approach again.

# #Datetime as index
no_2 = air_quality.pivot(index='datetime',columns='location',values='value')
# print(no_2)
# #By pivoting the data,the datetime information became the inde of the table.In general,setting 
# #a column as an index can be achieved by 'set_index()' function
# #Working with the a datetime index  provides powerful functionalities.For example,we do not need the 
# #'dt' accessor to get the time series properties,but have these properties available on the index directly.
# print(no_2.index.year)
# print(no_2.index.weekday)

# print(no_2.head())
# print(no_2.tail())
# #Create a plot of the No2 values in the different stations from the 20th of May till the end of 21st of June
# no_2['2019-05-20':'2019-06-21'].plot()
# plt.show()
# #By providing a string that parses to a datetime,a specific subset of the data can be select on a DatatimeIndex

# #Resample a time series to another frequency
# #Aggregate the current hourly time Series values to the monthly maximum value in each of the stations
# monthly_max = no_2.resample('M').max()
# print(monthly_max)
# #A very  powerful method on time series data with a datetime index,is the ability to resamplr() time 
# #series to another frequency.
# #The resample() method is similar to a groupby opetation:
# #it provides a time-based grouping,by using a string (e.g. 5H,...) that defines the target frequency
# #it requires an aggregation function such as mean(),max()...
# #Make a plot of daily median NO2 value in each of the station
no_2.resample('D').mean().plot(style='-o',figsize=(10,5))
plt.show()


