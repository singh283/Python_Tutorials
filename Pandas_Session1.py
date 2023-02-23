#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Pandas - The name is derived from the term - "Panel Data"  

# https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/

# High performance , easy  to  use data structure 
# Acts as data analysis tool in Python 

# Data structures available in Pandas :
    # 1. Series   -  1D labelled homogenous array ,  size immutable (means once a Series object is created operations such as appending/deleting which would change the size of the object are not allowed.) 
    # 2. DataFrame  -  General 2D labelled , size mutuable tabular structure with  potentially heterogeneously typed  columns.
    # 3. Panel   -  General 3D labelled ,  size mutable array  

# Advantage of Series over numpy array :
#     1. In Series we can create custom Index as opposed to default integer index in numpy array  .

# SET ROWS and COLUMNS to be viewed . 
# pd.set_option('display.max_rows', 101)
# pd.set_option('display.max_columns', 101)


# In[ ]:


# Points to be covered :
#   Operations on DataFrame :
#     a.  Reading and writing DataFrame
#     b.slicing DataFrame => [] ,  .loc[] , .iloc[]
#     c. applying filter and subsetting DataFrame => [Series_bool]
#     d. Adding new columns 
#     e. Deleting existing columns  
#     f. basic functions :  head().  tail() , info(),  describe(), reset_index() , rename(),  sort_values(),  append() 
    


# In[100]:


import pandas as pd

import warnings 
warnings.filterwarnings('ignore')


# In[3]:


# s = pd.Series()
# print(type(s))
# s


# In[4]:


# salary = [30000, 40000, 20000, 10000]
# salary


# In[5]:


# s = pd.Series(salary)
# s


# In[6]:


# Upcasting will be done in case any one element dataype differs as Series is 1D homogeneous array 

# s = pd.Series([30000, 40000, 20000.0, 10000])
# s


# In[7]:


# s = pd.Series([30000, 40000, '20000', 10000])
# s


# In[9]:


# In Pandas  and higher datastructures  ,  any datatype other than "int", "float" and "Time", "Datetime" will be considered as Object
# even string will be also considered as Object.

# s = pd.Series(['A', 'B' , 'C', '3000'])
# s


# In[14]:


# Index

# s = pd.Series(data = ['A', 'B' , 'C', '3000'], index = list('abcd')) # labels -  custom index 
# s


# In[15]:


# s = pd.Series(data = ['A', 'B' , 'C', '3000'], index = ['i', 'ii',  'iii', 'iv']) # labels -  custom index 
# s


# In[9]:


# Index in Series need not be Unique.

# s2 = pd.Series( range(10,20) , index = list('abcdefghia'))
# s2


# In[16]:


#  data as tuople object 

# s = pd.Series(('A', 'B' , 'C', '3000'))
# s


# In[19]:


#  data as dictionary object 

# s = pd.Series({'a':100, 'b':200 , 'c':300})
# s


# In[23]:


# Data as scalar value 
# here if we want to replicate the same value 'n' no of times then  we can give 'n' index and it will 
# assign the same scalar value for each index .

# s = pd.Series( data = 3 , index = ['a', 'b', 'c', 'd']  )
# s


# In[25]:


#  Accessing Elements in Series: 

# s = pd.Series( range(10,20) )
# s


# In[29]:


# print(s[0])
# print(s[9])
# print(s[0:5] , type(s[0:5])) # returns a Series object 10,11,12,13,14
# print(s[5:8])
# print(s[6:9])
# print(s[-1])  # negative index not works on Series .  


# In[3]:


# When we have a Series with custom index we have 2 ways of indexing, slicing 

# 1. By index 
# 2. By label  

# s1 = pd.Series( range(10,20) , index = list('abcdefghij'))
# s1


# In[37]:


# print(s1[0])  # Index by default value
# print(s1['a']) # Index by label 

# print()

# print(s1[4])
# print(s1['e'])

# print()

# # Slicing:
# print(s1[4:9]) # by Index [start:end] => end is exclusive
# print()
# print(s1['e':'i']) # by label [start:end] => end is INCLUSIVE 


# In[38]:


# print(s1[-2])  #  In case of index by label , -ve indexing is working on Series.


# In[44]:


# Operations on Series 
# Similar to ndarray objects , Series supports vector operations / broadcasting 

# s1 =  pd.Series(range(10,20))
# s2 =  pd.Series(range(30,40))

# print(s1)

# s1 + 4   #  supports Broadcasting


# In[43]:


# s1 > 15


# In[42]:


# s1 - s2


# In[9]:


# s1.value_counts()
# Return a Series containing counts of unique values.
# Series.count: Number of non-NA elements in a Series.

s1 = pd.Series( range(10,20) , index = list('abcdefghij'))
print(s1.value_counts())

print()
# s1.min(), s1.max()
# s1.where()
print(s1.where(s1>15))
print()

# Series.values 
# attribute returns Series as ndarray or ndarray-like depending on the dtype.
print(s1.values)
print()

s2 =  pd.Series(data = ['Boston', 'NewYork', 'Houston', 'Chicago'] )

s2.index = ['City1', 'City2', 'City3' , 'City4' ]

print(s2)
print()
print(s2.values , type(s2.values))

# s1.reset_index()

print()
print(s1.transpose())
# Return the transpose, which is by definition self.




# s1.append()
# s1.describe()
# Descriptive statistics include those that summarize the central
# tendency, dispersion and shape of a  dataset's distribution, excluding ``NaN`` values.

# returns Series or DataFrame, Summary statistics of the Series or Dataframe provided.
print()
print(s1.describe())

print()
# Series.keys() 
# Pandas Series.keys () function is an alias for index. It returns the index labels of the given series object.
print(s2.value_counts())
print()
print(s2.value_counts().keys())


# In[18]:


gender = pd.Series(['f', 'm','m', 'f', 'm' , 'f' , None , 'f'])
print(gender)

print()

gender1 = pd.Series([1,2,3,4, None , 5])
print(gender1)


# In[24]:


print(gender.unique())
print()
print(gender1.unique())


# In[25]:


print(gender.nunique())  #  does not take into consideration None/Null values  
print()
print(gender1.nunique())


# In[27]:


print(gender.isnull())
print()
print(gender1.isnull())


# In[28]:


print(gender.count())
print()
print(gender1.count())  # Return number of non-NA/null observations in the Series.


# In[32]:


print(gender.values , type(gender.values))
print()
print(gender1.values , type(gender1.values))


# In[41]:


print(gender1 + 4)
print(id(gender1  + 4 ))   # Broadcasting creates a NEW series object. 
print()  
print(gender1)
print(id(gender1))


# In[44]:


print(gender1)
print()

print(gender1>2)

print()

print(gender1[gender1>2])


# In[ ]:


# DataFrame


# In[45]:


df =  pd.DataFrame()
print(df, type(df))


# In[46]:


df = pd.DataFrame(data = range(10,15))
print(df)


# In[48]:


df = pd.DataFrame(data = range(10,15), columns= ['Col1'])
print(df)


# In[50]:


df = pd.DataFrame([[4,5], [6,9], [3,5], [7,8]], columns= ['col1', 'col2'])
df


# In[51]:


# In case of Nested list if any of the rows or columns have missing values then it will considered as NaN

df = pd.DataFrame([[4,5], [6,9,8], [3,5], [7,8]], columns= ['col1', 'col2', 'col3'])
df


# In[ ]:


# NaN - Not a number , in data analytics it represents missing values .
# NaN  --> in-built type 'float' type 

# Standalone column in a DataFrame has a property of Series , so all the elemnts within a column should be of same datatype 
# or if any of the elements is of different datatype then Upcasting happens to maintain homogenous property of Series.


# In[57]:


## DataFrame from dictionary 
# In case of creating DataFrame from dictionary, the keys of the dictionary represnted as columns
# In Case of dictionary we cannot have missing values , in case  there is no data we can impute np.NaN 


import numpy as np
df = pd.DataFrame( {'Name':['A', 'B' , 'C', 'D'] , 'Age':[27, 31, 28, 29] , 'Salary':['40000', 35000, 10000, np.NaN]} )
print(df)
print()
print('Column Name datatype : '   , df['Name'].dtype)
print('Column Age datatype : '    , df['Age'].dtype)
print('Column Salary datatype : ' ,df['Salary'].dtype)


# In[11]:


# creating DataFrame from list of dictionaries 

import numpy as np
import pandas as pd

df = pd.DataFrame( [ {'a':4},  {'a': 4 , 'b': 5} , {'c': 7} ] )
df


# In[15]:


# creating DataFrame from Series

df = pd.DataFrame( pd.Series(range(0,10)),  columns = ['col1'] )
df


# In[19]:


# Creating DataFrame from dictonary of list 

data = {'Name' : ['Tom', 'Jon', 'Kyle'] , 'Age': [24,27,25] }

df = pd.DataFrame( data , index = ['student1', 'student2', 'student3'] )
df


# In[3]:


# Reading data from external source 

df = pd.read_csv(r'C:\Users\amikumar61\OneDrive - Publicis Groupe\DS\EDA_Tutorial1\matches.csv')
df


# In[23]:


df.head()


# In[24]:


# Writing to External  source 

df.to_csv(r'C:\Users\amikumar61\OneDrive - Publicis Groupe\DS\EDA_Tutorial1\matches1.csv')


# In[101]:


# Operations on DataFrame 

ipl_data  = {'Team' : [ 'Riders' , 'Riders' ,'Devils' ,'Devils' , 'Kings', 'Kings' ,'Kings' , 'Kings', 'Riders' ,'Royals' ,'Royals' ,'Riders' ],
              'Rank': [1,2,2,3,3,4,1,1,2,4,1,2],
             'Year': [2014, 2015, 2014, 2015,  2014, 2015, 2016, 2017  , 2016, 2014, 2015, 2017 ],
              'Points': [876, 789, 863,  673, 741 , 812, 756, 788 , 694, 701, 804 , 690]}

df = pd.DataFrame(ipl_data)
df                     


# In[ ]:


# Accessing data from  DataFrame:

1. using []  operator 
2. using .loc[] operator 
3. using .iloc  operator 


# In[42]:


df['Team'] # Series 


# In[43]:


df.Team   # Series   (this method connot be used if column name does not have whietspace eg : Column  1)


# In[46]:


# select multiple columns 

df[['Team', 'Year']]   

# these are read operations , it will return new object. It does not make any change into original dataframe.
# using [[]] will always return a DataFrame . 


# In[47]:


df[['Team']]    # return object is a DataFrame


# # access  rows 4to 7(including) and cols Team and rank 

# In[49]:


# using []  operator 

df[['Team', 'Rank']][4:8]


# In[50]:


# using .loc operator 
# syntax <DataFrame>.loc[range_rows, range_cols ] => .loc[r0:rn , c0:cn] =>  .loc[ [r0,r1....rn] , [c0,c1....cn] ]
# Note : need to specify r0,r1,r2 ....rn , c0,c1, ....cn  as LABELS, by default if we do not pass the custom index 
# for labels then default index behaves as LABELS 

# df.loc + colon 
df.loc[4:7, 'Team':'Rank']


# In[4]:


# df.loc + [] (with list of range of rows and columns  ) 

df.loc[[4,5,6,7] , ['Team','Rank']]


# In[5]:


# using .iloc operator 
# syntax <DataFrame>.iloc[range_rows, range_cols ] => .iloc[r0:rn , c0:cn] =>  .iloc[ [r0,r1....rn] , [c0,c1....cn] ]
# Note : need to specify r0,r1,r2 ....rn , c0,c1, ....cn  as default index 

# df.iloc + colon 

df.iloc[4:8, 0:2]   # index 


# In[6]:


# df.iloc + [] (with list of range of rows and columns  ) 

df.iloc[ [4,5,6,7 ], [0,1] ]   # index 


# In[14]:


print(df['Team'] == 'Riders')
print()
print(df.Team == 'Riders')

print()

print(df[df['Team'] == 'Riders'])
print()
print(df[df.Team == 'Riders'])


# In[17]:


df[df.Team == 'Royals']


# In[27]:


# DataFrame Subset  :

## SELECT all the recs where Team = Kings and rank =2 

df[df.Team == 'Kings'][df.Rank == 1]


# In[23]:


df[(df.Team == 'Kings') & (df.Rank == 1)]


# In[30]:


## SELECT "Year" where Team = Kings and rank =1  

df[df.Team == 'Kings'][df.Rank == 1]['Year']


# In[38]:


df[df.Team == 'Kings'][df.Rank == 1]['Year']


# In[35]:


df[(df.Team == 'Kings') & (df.Rank == 1)].iloc[:,2:3]


# In[37]:


df[(df.Team == 'Kings') & (df.Rank == 1)].loc[6:7,'Year']


# In[39]:


df


# In[42]:


df[df.Points > 700]


# In[43]:


df[~(df.Points > 700)]  ## Opposite where Points > 700 


# In[49]:


df[df.Team == 'Kings'][df.Rank == 1][['Year', 'Points']]


# In[59]:


# Adding new column to a DataFrame 

df['Year_dup'] = df['Year']
df


# In[60]:


df['new_col'] = 0
df


# In[3]:


df['new_col'] = 5
df


# In[7]:


# DELETE columns from DataFrame using drop:
# axis = 0 => by row ; axis = 1 => by col  
# Need to use inplace = True in order to reflect the changes in original DataFrame

df.drop('new_col', axis = 1 , inplace = True) 
df


# In[8]:


df.drop(10, axis = 0 , inplace = False) 


# In[11]:


df['col1'] = df.Points * 2

df

df['col2'] = 5
df


# In[13]:


# DELETE multiple rows and columns 

df.drop(['col1' ,  'col2' ] , axis = 1 , inplace = True)
df


# In[17]:


# Adding new row to the DataFrame 

df.append({'Team': 'Riders' , 'Rank': 4, 'Points' : 600}, ignore_index = True )


# In[18]:


df


# In[ ]:


#  Basic functionalities :
#  head() , tail() , sample() , info(), sort_values() , columns , rename() , describe()


# In[19]:


df.sample(3)  # Return a random sample of items from an axis of object.


# In[6]:


df.columns #  Names of column   and  it is an iterable  


# In[7]:


# Rename column  'Points' to 'Scores'
df.rename(columns = {'Points': 'Scores'} , inplace = True )

df


# In[8]:


df.sort_values(by  = 'Team', ascending = True)


# In[9]:


df.sort_values(by  = 'Team', ascending = True).head()


# In[12]:


df.sort_values(by = 'Team' , ascending = False)


# In[15]:


# Sort on "Team" in descending order and "Rank" in ascending order 

df.sort_values(by = ['Team', 'Rank'], ascending = [False ,  True] ,  inplace = True  )


# In[16]:


df


# In[34]:


# To again reset  the index level 
# Reset the index of the DataFrame, and use the default one instead 

df.reset_index(inplace = True)


# In[22]:


# <DataFrame>.info() 
# This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.

df.info()


# In[23]:


df.describe()  #  statistical summary of the data 


# In[24]:


# UDF (user defined function) on DataFrame :

# apply() --> works on Series , DataFrame  row-wise /  column wise / element wise 


# In[28]:


import numpy as np
def  mean_(col):
    ''' Returns avg of given data'''
    return np.mean(col)


# In[39]:


df


# In[44]:


df[['Scores']].apply(mean_, axis = 0)


# In[47]:


df[['Scores' , 'Rank', 'Year']].apply(mean_, axis = 0)


# In[49]:


# Perform the mapping on Team : 'Riders' -->  1 , 'Devils' --> 2 , 'Royals' --> 3 ,Kings' -->  4 

df['Team_Mapp']  = df.Team.apply(lambda t: 1 if t == 'Riders' else 2 if t == 'Devils' else 3 if t == 'Royals' else 4)  
df


# In[48]:


def map_(col):
    print(col , type(col))
    if col == 'Riders':
        col = 1
    elif col == 'Devils':
        col = 2
    elif col ==  'Royals':
        col = 3
    else:
        col = 4
    return col



df['Team_Map1'] =  df.Team.apply(map_)


# In[50]:


df


# In[56]:


import numpy as np 
df[['Rank', 'Points']].apply(lambda x: np.mean(x) )  # By default axis = 0 by column   
df[['Rank', 'Points']].apply(lambda x: np.mean(x) , axis  = 1 ) # by row  


# In[93]:


def mean_(col):
    print(col, type(col))
    return col.mean()

df.Rank.apply(mean_ )  
# --> this will give error as col is "int" (AttributeError: 'int' object has no attribute 'mean')
# Here since we are doing  operation on  a series , col is taking  single element of Series which  is of type int 
# and there is no method mean() for int .


# In[94]:


df[['Rank']].apply(mean_)
#  this will work as we are doing operation on DataFrame and passing col as Series object  


# In[95]:


def mult_(col):
    print(col, type(col))
    return col*2

df.Rank.apply(mult_ )     #  In case of Series "elementwise"  operation is performed .


# In[96]:


df[['Rank']].apply(mult_ )  # Here broadcasting is happening 


# In[97]:


#  applymap() -- Apply a function to a Dataframe elementwise.
df[['Rank']].applymap(mult_ )


# In[119]:


# Aggregate functions - sum , avg , min , max 

print(df.Points.sum())
print(np.sum(df.Points))

df[['Team', 'Points']].apply(lambda x: )

