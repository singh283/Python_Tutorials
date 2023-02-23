#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import seaborn as sns 


# In[ ]:


# Matplotlib and Seaborn 

# Matplotlib is a plotting library in Python 
# One of the greatest benefits of visualization is that it allows us visual access to huge amounts of data in 
# easily digestible visuals. 
# Matplotlib consists of several plots like line, bar, scatter, histogram etc.

# Seaborn is built on top of Matplotlib and supports plotting charts with minimal code as compared to matplotlib.

# Installation :
#     !pip install matplotlib 
#     !pip install seaborn
    
# Different types of  chart: 

# For different visualisations using Matplotlib  refer  to https://matplotlib.org/stable/gallery/index.html
# https://seaborn.pydata.org/examples/index.html


# In[16]:


# !pip show matplotlib

# !pip install matplotlib --upgrade


# In[3]:


df = pd.read_csv('dataset_3.csv')
df.head()


# # Let's learn Matplotlib and Seaborn through asnwering the following questions.,
#     #    1 (a). How many records belongs to each Pclass. (bar-chart/histogram),
#     #    1 (b). How many passengers survived. (bar-plot/countplot),
#     #    1 (c). Percentages of passengers who survived.,
#     #    2. Display statistical summary of Age and Fare. (boxplot),
#     #    3. Display density distribution of Age. (Swarmplot/Violinplot),
#     #    3. What is the relation between Age and Fare (Linear/Non-linear/no relationship)? (scatterplot/Pairplot),
#     #    4. Distribution of Fare. (check if Fare represents bell-shaped curve) (histogram/distplot),
#     #    5. Identify strongly correlated columns. (Heatmap),
#     #    6. Display Q1 and Q2 on same plot area (subplots)#

# In[12]:


print(df.Pclass.unique())
print(df.Pclass.value_counts())
print(df.Pclass.dtype)


# In[14]:


#    1 (a). How many records belongs to each Pclass. (bar-chart/histogram)
# Using Matplotlib

plt.bar( x = [str(i) for i in df.Pclass.unique()] ,height = df.Pclass.value_counts() )
plt.xlabel('Pclass')
plt.ylabel('Passenger Count')
plt.title('Bar plot of Pclass', fontsize = 15 )
plt.show()


# In[18]:


# Using Seaborn 

sns.countplot(df.Pclass )
plt.title('Bar plot of Pclass', fontsize = 15 )
plt.show()


# In[19]:


#    1 (b). How many passengers survived. (bar-plot/countplot)

sns.countplot(df.Survived ,)
plt.show()


# In[24]:


# %age of Passengers who survived and not survived

df.Survived.value_counts()/df.shape[0]*100


# In[25]:


df.describe()  # 5 Points summary 


# In[14]:


df.dtypes


# In[27]:


#  Display statistical summary of Age and Fare (BOX PLOT)

plt.figure(figsize = (10,4))
plt.boxplot(df.Age , vert=False)
plt.title('Box plot for age')
plt.show()


# In[29]:


plt.figure(figsize = (10,4))
sns.boxplot(df.Age)
plt.title('Box plot for age')
plt.show()


# In[40]:


#  Display density distribution of Age (Swarmplot/ Violin plot)

# Swarmplot is only available in Seaborn
# A swarm plot is a type of scatter plot that is used for representing categorical values

plt.figure(figsize = (20,4))
sns.swarmplot(df.Age) 
plt.title('Age Swarm Plot')
plt.show


# In[37]:




plt.figure(figsize = (20,4))
sns.swarmplot(df.Age , df.Fare , hue = 'Survived' , data = df) 
plt.title('Age Swarm Plot')
plt.show


# In[39]:


# Violin Plot  (SwarmPlot + BoxPlot )

plt.figure(figsize = (20,4))
sns.violinplot(df.Age)
plt.title('Age Violin Plot')
plt.show


# In[11]:


#  What is the relation between Age and Fare (Linear/Non-linear/no relationship)? (scatterplot/Pairplot)

sns.scatterplot(x= df.Age , y = df.Fare , hue = 'Survived', data =df)
plt.title('Scatter Plot for relnship b/w Age and Fare' , fontsize = 15)
plt.show()

# Here we can see that there is no relationship between Fare and age .


# In[25]:


sns.scatterplot(df.Age , df['Siblings/Spouses Aboard'] , hue = 'Survived', data = df )
plt.title('Scatter Plot for relnship b/w Age and Siblings/Spouses Aboard' , fontsize = 15)
plt.show()


# In[12]:


# pairplot - his function will create a grid of Axes such that "each numeric variable" in data 
# will by shared across the y-axes across a single row and the x-axes across a single column.

sns.pairplot(df)


# In[16]:


df.columns


# In[27]:


cols = ['Survived', 'Pclass',  'Age',  'Fare']

cols1 = ['Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Siblings/Spouses Aboard',
       'Parents/Children Aboard', 'Fare']

sns.pairplot(df[cols1] , hue = 'Survived' ,  data= df)   
# In pairplot cols 'Name' and 'Sex'  is not considered as it is not of numeric datatype


# In[30]:


# Distribution of Fare. (check if Fare represents bell-shaped curve) (histogram/distplot)

plt.hist(df.Fare , bins = 20) #  here bins divide the complete spread of data into 20 buckets 
plt.xlabel('Fare')
plt.ylabel('Count')
plt.show()


# In[28]:


sns.distplot(df.Fare)
plt.show()


# In[31]:


sns.histplot(df.Fare)


# In[46]:


# Pearson's Correlation Coefficient [-1 , 1 ] (Linear relations)
#  measures the statistical relationship, or association, between two continuous variables. 
# Degree of  Linear  relationship  between 2 variables 
# Direction --> sign 
# Magnitude -->  strength
# 1 --> Perfect Linear relationship
# (1, 0.75] --> strong linear relationship
# (0.75, 0.5) --> Moderate linear relationship
# < 0.5 --> Weak Linear relationship
# 0 --> No relationship

# It is known as the best method of measuring the association between variables of interest because it is based on the method of covariance.
# It gives information about the magnitude of the association, or correlation, as well as the direction of the relationship.

df.corr()


# In[48]:


# HeatMap  

# Identify strongly correlated columns. (Heatmap)
# one of the uses for a heatmap — the correlation matrix heatmap. 
# A correlation matrix allows us to identify how well, or not so well, features within a dataset correlate with each other 
# as well as whether that correlation is positive or negative.

sns.heatmap(df.corr())


# In[50]:


sns.heatmap(df.corr(), annot= True)


# In[52]:


# Display Q1 and Q2 on same plot area (subplots)

fig , axes = plt.subplots(1,2 , figsize = (20,4))


# In[56]:


fig , axes = plt.subplots(1,2 , figsize = (20,4))

sns.distplot(df.Age, ax = axes[0])
axes[0].set_title('Age Distribution')

sns.distplot(df.Fare, ax = axes[1])
axes[1].set_title('Fare Distribution')


# In[69]:


fig , axes = plt.subplots(2,2 , figsize = (20,10))

sns.distplot(df.Age, ax = axes[0, 0])
axes[0, 0].set_title('Age Distribution')

sns.distplot(df.Fare, ax = axes[0 ,1])
axes[0, 1].set_title('Fare Distribution')

sns.distplot(df.Age, ax = axes[1, 0])
axes[1, 0].set_title('Age Distribution')

sns.distplot(df.Fare, ax = axes[1,1])
axes[1, 1].set_title('Fare Distribution')


# In[67]:


fig.savefig('Example_Plot.jpg')  # Saves the plot as JPG   


# In[66]:


fig , axes = plt.subplots(1,2 , figsize = (20,4))

axes[0].hist(df.Age)   #  In case of  Matplotlib we use axes[].function 
axes[0].set_title('Age Distribution')

sns.distplot(df.Fare, ax = axes[1])
axes[1].set_title('Fare Distribution')


# In[68]:


fig


# # For different visualisations using Matplotlib  refer  to https://matplotlib.org/stable/gallery/index.html
# https://seaborn.pydata.org/examples/index.html
