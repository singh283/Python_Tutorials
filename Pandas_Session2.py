#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


# In[ ]:


# Pandas group by 
    # is used to perform group level operations
    # 3 types of group level operations supported by pandas groupby
        # 1. aggregation : sum, max, min, count, average
        # 2. transformation
        # 3. filter

    # any groupby operationsa are performed at three steps:
        # 1. splitting the data 
        # 2. operation
        # 3. combining the results


# In[2]:


ipl_data  = {'Team' : [ 'Riders' , 'Riders' ,'Devils' ,'Devils' , 'Kings', 'Kings' ,'Kings' , 'Kings', 'Riders' ,'Royals' ,'Royals' ,'Riders' ],
              'Rank': [1,2,2,3,3,4,1,1,2,4,1,2],
             'Year': [2014, 2015, 2014, 2015,  2014, 2015, 2016, 2017  , 2016, 2014, 2015, 2017 ],
              'Points': [876, 789, 863,  673, 741 , 812, 756, 788 , 694, 701, 804 , 690]}

df = pd.DataFrame(ipl_data)
df 


# In[7]:


# fIND THE average of Points for each Team :

lst = []
for team in df.Team.unique():
    t = df[df.Team == team]['Points']  # Splitting the  data
    t =  t.mean()
    lst.append({team : t})
lst


# In[11]:


df.groupby('Team')['Points'].mean()  # returning Series 


# In[12]:


df.groupby('Team')[['Points']].mean() # returning DataFrame


# In[15]:


df.groupby('Team')[['Points']].mean().rename(columns  = {'Points' : 'Avg_Points'})


# In[16]:


df.groupby('Team')[['Points']].mean().rename(columns  = {'Points' : 'Avg_Points'}).reset_index()


# In[23]:


df.groupby('Team')[['Points', 'Rank']].mean().rename(columns = {'Points' : 'Avg_points' , 'Rank' :'Avg_Rank'}).reset_index()


# In[25]:


# Doing Groupby using multiple columns 

df.groupby(['Team' , 'Rank'])['Points'].mean()


# In[39]:


df.groupby(['Team' , 'Rank'])[['Points']].mean()  # Multi Index DataFrame (Team, Rank)


# In[40]:


df.groupby(['Team' , 'Rank'])[['Points']].mean().reset_index()


# In[51]:


# Example of different aggregate on different columns : 
# Compute average of 'Points' and Maximum of 'Rank()' for each  team.

df.groupby('Team')['Points', 'Rank'].agg({'Points': 'mean' , 'Rank' : 'max'}).rename(columns = {'Points': 'Avg_Points' , 'Rank' : 'Max_Rank'}).reset_index()


# In[72]:


#  get avg of Points per Team and save as new column to df 

df['Avg_Points'] =  df.groupby('Team')['Points'].mean()
df

# here we see we are getting all values as 'NaN' for the new column IOF avg of Points value . 
# This is so becoz the length of the  df's (no of rows ) are not the same.


# In[74]:


df.drop('Avg_Points' , axis = 1 , inplace = True)


# In[77]:


# Groupby Transform 
# Call ``func`` on self producing a DataFrame with the same axis shape as self.
# Returns : A DataFrame that must have the same length as self. 

# df.transform()

df.groupby('Team')['Points'].transform('mean')


# In[78]:


df['Avg_Points'] = df.groupby('Team')['Points'].transform('mean')
df


# In[83]:


df.Points/df.groupby('Team')['Points'].transform('mean')


# In[84]:


df.groupby('Team')['Points'].transform(lambda x: x/ x.mean())


# In[89]:


df[['Avg_Points' , 'Avg_Rank']]  = df.groupby('Team')['Points', 'Rank'].transform(lambda x: x/ x.mean())
df  


# In[19]:


# Groupby Filter 
# In case of "filter" unlike "transform" we need to make sure that evaluated expression retruns bool value .

# Select details of those team who  have played more than 2 yrs 

print(df.groupby('Team').filter(lambda row : print(row)))
print()

df.groupby('Team').filter(lambda row : len(row) >  2).sort_values(by = ['Team', 'Rank'])


# In[13]:


print(len(df))
print(df.shape)
print('length  of DataFrame is : ' , df.shape[0])
print('Width  of DataFrame is : ' , df.shape[1])


# In[17]:


# Select Rank of those team who  have played more than 2 yrs 

df.groupby('Team').filter(lambda x : len(x) > 2 )['Rank']
# OR 
df.groupby('Team')['Rank'].filter(lambda x : len(x) > 2 )


# In[20]:


df


# In[96]:


df['Avg_Points'] =  df.groupby('Team')['Points'].transform(lambda x : x/x.mean())


# In[103]:


# Doing the sorting of the DataFrame based on Avg_Points  

df.sort_values(by = 'Avg_Points' , ascending = False )


# In[ ]:


# Pandas Merge: 

# pd.merge()  -- Merge DataFrame or named Series objects with a database-style join. 

# Returns
# -------
# DataFrame
#     A DataFrame of the two merged objects.


# In[24]:


df1 = pd.DataFrame({ 'id' : [1,2,3,4,5] ,
                          'Name' : ['Alex', 'Amy', 'Allen' , 'Alice', 'Ayoung'] ,
                          'subject_id' : ['sub1', 'sub2', 'sub4', 'sub6', 'sub5',]
                       })
df2 = pd.DataFrame({ 'id' : [1,2,3,4,5] ,
                          'Name' : ['Billy', 'Brian', 'Bran' , 'Bryce', 'Betty'] ,
                          'subject_id_right' : ['sub2', 'sub4', 'sub3', 'sub6', 'sub5',]
                       })

df3 = pd.DataFrame({ 'id' : [1,2,3,5] ,
                          'Name' : ['Jon', 'Rose', 'Mike' , 'Tom'] })

# adding a new row in df1 and df2  
df1 = df1.append( {'id' : 6 , 'Name' : 'XYZ',  'subject_id' : 'sub11'} , ignore_index= True)

df2 = df2.append( {'id' : 11 , 'Name' : 'ABC',  'subject_id_right' : 'sub7'} , ignore_index= True )


# In[4]:


df1


# In[5]:


df2


# In[13]:


# 1.  Merge on id 

pd.merge(df1 , df2 , on = 'id' ,  suffixes= ('_left', '_right') )


# In[14]:


df1.merge(df2 , on ='id')


# In[ ]:


# To merge more than 2 DataFrame , will have to do chaining of merge 

# df1.merge(df2).merge(df3).merge(df4) ....... .merge(dfn)


# In[8]:


# 2.  Merge on id and subject_id 

pd.merge(df1 , df2 , left_on = ['id', 'subject_id'] , right_on = ['id', 'subject_id_right'] )


# In[9]:


# 3. Perform left join on key =id 

pd.merge(df1 , df2  , how = 'left' , on = 'id' )


# In[10]:


# 4. Perform right join on key =id 

pd.merge(df1, df2 , how = 'right' , on = 'id')


# In[11]:


# 5. Perform outer join on key =id 

pd.merge(df1, df2 , how = 'outer' , on = 'id')


# In[12]:


# 6. Perform left join on key =id , subject_id 

pd.merge(df1, df2 , how = 'left' , left_on = ['id' , 'subject_id'] , right_on =  ['id' , 'subject_id_right'])


# In[15]:


# 7. Perform right join on key =id , subject_id 
pd.merge(df1, df2 , how = 'right' , left_on = ['id' , 'subject_id'] , right_on =  ['id' , 'subject_id_right'])


# In[16]:


# 8. Perform right join on key =id , subject_id 

pd.merge(df1, df2 , how = 'outer' , left_on = ['id' , 'subject_id'] , right_on =  ['id' , 'subject_id_right'])


# In[18]:


# Pandas Concat 

pd.concat([df1 , df2 ], axis = 0  )


# In[19]:


pd.concat([df1 , df2 ], axis =1 )


# In[28]:


pd.concat([df1, df3] , axis  = 0)


# In[29]:


pd.concat([df1, df3] , axis  = 1)


# In[ ]:





# In[ ]:




