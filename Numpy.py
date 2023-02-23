#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Numpy - Numerical python - library consisiting of  multidimesional array objects and collection of routines to process 
# the array 

# The need for NumPy arises when we are working with multi-dimensional arrays. 
# The traditional array module does not support multi-dimensional arrays

# Comparison of Numpy array over List 
# https://www.geeksforgeeks.org/python-lists-vs-numpy-arrays/ 
  

# Using Numpy we can do mathematical and logical operations on array.
# Fourier transforms and routine for shape manipulation.
# Operations related to  Linear algebra and random number generation.

# Originally Python was not designed for numeric computation. 
# As people started using python for various tasks, the need for fast numeric computation arose. 
# And the Numpy was created by a group of people in 2005 to address this challenge.

# https://www.scaler.com/topics/2d-array-in-python/ 

1. Numpy array is a collection of similar data-types that are densely packed in memory. 
    A Python list can have different data-types, which puts lots of extra constraints while doing computation on it.

2. Numpy is able to divide a task into multiple subtasks and process them parallelly.
3. Numpy functions are implemented in C. Which again makes it faster compared to Python Lists.


# In[1]:


import numpy as np


# In[106]:


arr11 = np.array([ [1,2,3] ])

print(arr11)
print(arr11.shape)
print(arr11.ndim)
print(arr11.size) # total no of elements in array


# In[90]:


arr0 = np.array([1,2,3])
print(arr0.shape)

print(arr0.ndim)


# In[94]:


arr = np.array([ [1,2,3] , [4,2,5] , [9,10,11] ] )

arr


# In[4]:



print(arr)


# In[5]:


print(type(arr))


# In[7]:


print(arr.shape)


# In[18]:


print(arr.ndim)


# In[12]:


arr1 = np.array( [ [ [1,2,3] , [4,2,5] , [10,11,13] ]  ] )

arr1


# In[20]:


print(arr1.ndim)
print(arr1.shape)


# In[16]:


arr2 = np.array( [ [ [1,2,3] , [4,2,5] , [10,11,13] ] , [ [9,8,7] , [15,12,14] ,  [20,21,22]] ]  )
                  
arr2


# In[21]:


print(arr2.ndim)
print(arr2.shape)


# In[27]:


arr4 = np.array([ [] ])

print(arr4.ndim)


# In[81]:


arr5 = np.array( [ [   [1,2,3] , [4,5,6] ] ,  [ [0,0] , [1,1] ] ]  )
print(arr5)
print(arr5.ndim)
print(arr5.shape)
print(arr5.dtype)


# In[79]:


arr5 = np.array( [ [   [1,2,3] , [4,5,6] ] ,  [ [0,0] , [1,1] ] ]  , dtype=object )
print(arr5)
print(arr5.ndim)
print(arr5.shape)
print(arr5.dtype)


# In[82]:


arr5 = np.array( [ [   [1,2,3] , [4,5,6] ] ,  [ [0,0,0] , [1,1,1] ] ]   )

print(arr5)
print(arr5.ndim)
print(arr5.shape)


# In[64]:


lst = [2000, 3000, 4000, 5000]

arr_lst =  np.array(lst)
print(arr_lst)
print(arr_lst.ndim , arr_lst.shape , arr_lst.dtype)
arr_lst


# In[109]:


# Upcasting : 

# Python automatically converts one data type to another data type. 
# This process doesn’t need any user involvement Python promotes the conversion of lower data type, 
# for example, integer to higher data type says float to avoid data loss. 
# This type of conversion or type casting is called UpCasting

lst1 = [2000, 3000, 4000, 5000.0]
arr_lst1 =  np.array(lst1)
print(arr_lst1)
print(arr_lst1.ndim , arr_lst1.shape , arr_lst1.dtype)
arr_lst1


# In[67]:


lst2 = [2000, 3000, 4000, 5000.0, 'amit']
arr_lst2 =  np.array(lst2)
print(arr_lst2)
print(arr_lst2.ndim , arr_lst2.shape , arr_lst2.dtype)
arr_lst2


# In[69]:


lst3 = [[2000, 3000 ] , 4000, 5000.0, 'amit']
arr_lst3 =  np.array(lst3)
print(arr_lst3)
print(arr_lst3.ndim , arr_lst3.shape , arr_lst3.dtype)
arr_lst3


# In[73]:


lst3 = [[2000, 3000 ] , 4000, 5000.0, 'amit']
arr_lst3 =  np.array(lst3, dtype=object)
print(arr_lst3)
print(arr_lst3.ndim , arr_lst3.shape , arr_lst3.dtype)
arr_lst3


# In[114]:


#  Ways to create an array object using numpy packages 

# print(dir(np))

# np.array()
# np.ones()
# np.zeros()
# np.empty()
# np.linspace()   - Generates only 1D array 
# np.arrange()    - Generates only 1D array 
# np.random.rand*()


# In[128]:


# np.empty() - Return a new array of given shape and type, without initializing entries. 

arr1 = np.empty(5)
print(arr1)
print('Array element datatype : ', arr1.dtype)
print('Shape of array :' , arr1.shape )
print('Type of  arr1 :' , type(arr1))
print('Size/ total no of elements  of array :' , arr1.size)
print('Dimension of array : ' , arr1.ndim)


# In[129]:


arr2 = np.empty((5,2))   
print(arr2)
print('Array element datatype : ', arr2.dtype)
print('Shape of array :' , arr2.shape )
print('Type of  arr2 :' , type(arr2))
print('Size/ total no of elements  of array :' , arr2.size)
print('Dimension of array : ' , arr2.ndim)


# In[130]:


arr2 = np.empty((5, 2, 3))    # 3D array 
print(arr2)
print('Array element datatype : ', arr2.dtype)
print('Shape of array :' , arr2.shape )
print('Type of  arr2 :' , type(arr2))
print('Size/ total no of elements  of array :' , arr2.size)
print('Dimension of array : ' , arr2.ndim)


# In[132]:


arr2 = np.ones(10)   
print(arr2)
print(arr2.dtype)


# In[135]:


arr2 = np.ones((5,3))  
print(arr2)
print(arr2.dtype)


# In[137]:


arr2 = np.zeros((5,5))  
print(arr2)
print(arr2.dtype , type(arr2))


# In[141]:


# np.arange([start], stop ,[step])-  Return evenly spaced values within a given interval.

# arange always gives ONLY 1D array

# return type - ndarray
# start - 0
# step - 1

arr2 = np.arange(4,10)  
print(arr2)
print(arr2.dtype , type(arr2))


# In[144]:


arr2 = np.arange(10,-10, -1)  
print(arr2)
print(arr2.dtype , type(arr2))


# In[146]:


arr2 = np.arange(10, step = 2)  
print(arr2)
print(arr2.dtype , type(arr2))


# In[160]:


for i in np.arange(10, step = 2) :
    arr = np.array([ [i, i, i] , [i,i,i] ])

arr


# In[162]:


# np.linspace() - returns an ndarray with evenly spaced values over specified interval.

# By feault it generates  50  elements which are evenly spaced over specified interval.
# np.linspace always gives ONLY 1D array

arr = np.linspace(0,10)

print(arr)
print(arr.dtype , type(arr))


# In[163]:


arr = np.linspace(0,10, 20)

print(arr)
print(arr.dtype , type(arr))


# In[165]:


# np.random.rand*

# np.random.randint() -- # Return random integers from `low` (inclusive) to `high` (exclusive).
# 

for i in range(10):
    print(np.random.randint(6))


# In[166]:


for i in range(10):
    print(np.random.randint(2, 6))  # [2,6)  -  all elements will be >= 2 and <6


# In[167]:


arr = np.random.randint(2,8, 10)  # [2,8) - returns array having total 10 elments >=2 and < 8 

print(arr)
print(arr.dtype , type(arr))


# In[168]:


arr = np.random.randint(2,8, (5,2))  # [2,8) - returns 2D array of 5 rows  and 2 cols having elments >=2 and < 8 

print(arr)
print(arr.dtype , type(arr))


# In[171]:


# array using np.random.rand()

# Create an array of the given shape and populate it with
# random samples from a uniform distribution
# over ``[0, 1)``.
        
arr = np.random.rand(10)
print(arr)

print()
        
arr = np.random.rand(5,2)
print(arr)


# In[173]:


# array using np.random.randn()

# Return a sample (or samples) from the "standard normal"  (Gaussian) distribution.

arr = np.random.randn(5,3)
print(arr)
print()
print(arr.dtype ,  type(arr),  arr.shape , arr.size )


# # Comparing List vs Array for computational speed 

# In[235]:


import timeit as tt
# Time execution of a Python statement or expression 

get_ipython().run_line_magic('pinfo', 'timeit')


# In[178]:



py_lst =  [  i for i in range(100000)]
start = tt.timeit()

py_lst = [i+2  for i in range(100000)]

end = tt.timeit()

print('Elapsed time : ', round((end - start) , 5))


# In[181]:


arr =  np.array([ i for i in range(100000)])
print(arr.shape, arr.ndim)

start = tt.timeit()

arr += 2 

end = tt.timeit()

print('Elapsed time : ', round((end - start) , 5))


# In[183]:


arr = np.linspace(0,10, 20)

print(arr)
print(arr.dtype , type(arr), arr.ndim)


# In[212]:


# Reshape() -  Returns an array containing the same data with a new shape.

arr.reshape(5,4)

arr.reshape(20,1)


# In[213]:


np.reshape(arr, (5,4))


# In[220]:


# reshape will not do the transformation on original array 

#  In Case where we are using "np.arange()"" OR "np.linspace" which always returns 1D array and our requirement is to have 
#  hihger dimension of that returned array , there we can make use of np.reshape()

print(arr)
print() 
arr1 =  np.reshape(arr , (2,5,2))

print(arr1)
print()
print(arr1.ndim , arr.shape, arr.size)


# In[231]:


arr = np.random.rand(5,2)

# ravel()

print(arr)    #  this is 2D array , now with  the help of ravel function -- return a contiguous flattened array.;
#  however this does not change the orignal array  

print('\n\n  After applying  np.ravel() \n\n')

print(arr.ravel())

# Result  is flattened 1D array 


# In[251]:


# Operations on  array  objects ..

bonus = [45000, 34000, 55000]
salary = [89000, 43000, 12000]

x = zip(bonus , salary)   

# A zip object yielding tuples until an input is exhausted. 

print(tuple(x))

[ x+y for x , y in zip(bonus, salary) ]


# In[252]:


bonus = [45000, 34000, 55000]
salary = [89000, 43000, 12000]

print(np.array(bonus))
print(np.array(bonus))

np.array(bonus) + np.array(salary)

# Numpy  array  objects supports vector operations (in above case Element wise addtion )


# In[253]:


print(2*[30000, 40000, 60000])
print(2*np.array([30000, 40000, 60000]))  # element wise multiplication


# In[254]:


arr -arr


# In[255]:


arr/arr


# In[256]:


arr1 = np.array([200,  300, 400])
arr2 = np.array([2,  3 ])

arr1 * arr2  # valueError: operands could not be broadcast together with shapes (3,) (2,) 


# In[257]:


arr1 = np.array([200,  300, 400])
arr2 = np.array([2,  3 , 4])

arr1 *  arr2


# In[267]:


# Accessing elements of an array  

arr = np.arange(1,10)

print(arr)

print(arr[0])
print(arr[4])
print(arr[2])
print(arr[-1])
print(arr[-len(arr)])
print(arr[0:4]) # retrun will be array[1 2 3 4]
print(arr[:])
print(arr[-1:-3:-1])
print(arr[:4])
print(arr[4:4]) # array[]
print(arr[4:5])


# In[280]:


arr = np.linspace(0,10, 20).reshape(4,5)

print(arr)

print(arr[0][0])
print(arr[0,0])
print(arr[2,1])

print(arr[0][1:3])
print(arr[0,1:3])

print(arr[0:2][1:3]) #  ThiS won't work so use as below (it has range for rows as well as columns )

# NOTE : Other than  1D  indexing(chain/list indexing [i][j]) for higher dimesnions we should use Matrix indexing [i,j]

print(arr[0:2,1:3]) 


# In[286]:


# Comparison Operator 

print(arr)

print()

print(arr > 4 )

print()


print(arr[arr > 4]) # retruns 1D array  


# In[6]:


# in-built methods  

# print(dir(np))
arr =  np.arange(1,11).reshape(2,5)

# np.where(condition , [x,y])   
# Returns an array with elements from `x` where `condition` is True, and elements
# from `y` elsewhere.

print("**** np.where() ****")
print(arr)
print()
print(np.where(arr > 4 , arr ,  0) ) 

# here wherever the elements satisfies the condition those are filtered 
#  and rest which do not satisfy will have value as  0 

print()

# np.max()
# Returns the indices of the maximum values along an axis. 

print("**** np.max() ****")
print(np.max(arr))  
print()

print(np.max(arr , axis = 0 ))  
print()

print(np.max(arr , axis = 1))

# np.argmax()
# Returns the indices of the maximum values along an axis.
print()
print("**** np.argmax() ****")
print(np.argmax(arr))

# np.min()
# Return the minimum of an array or minimum along an axis.

print()
print("**** np.min() ****")
print(np.min(arr))
print(np.min(arr, axis = 0))
print(np.min(arr, axis = 1))

#  np.sort(a ,) 
#  Returns a sorted copy of an array.
#  a : array_like
#      Array to be sorted.

print()
print("**** np.sort() ****")
print(np.sort([4,9,7,6]))

# np.shape()

# Return the shape of an array.
# return type is a tuple of int 
print()
print("**** np.shape() ****")
print(np.shape(arr))

# np.corrcoef() 
# The correlation coefficient matrix of the variables.
# A correlation is a relationship between two random variables basically with respect to statistics.
# A correlation coefficient is a statistical measure of the change in one variable defined by another variable.

print()
print("**** np.corrcoef() ****")
arr1 = np.arange(11,21).reshape(2,5)
print(arr1)
print()
print(np.corrcoef(arr, arr1))

# np.all()
# Test whether all array elements along a given axis evaluate to True.
# If all elements are non zero  then  np.all() returns True.

print()
print("**** np.all() ****")
print(np.all(arr))

print()

a = np.array([ [0,1,2], [2,3,1] ])
print(a)
print()
print(np.all(a))
print(np.all(a, axis = 0))
print(np.all(a, axis = 1))

a1 = np.array([ [1,1,2], [2,3,1] ])
print(a1)
print()
print(np.all(a1))


# np.any()
# Test whether any array element along a given axis evaluates to True.
# If any of the elements is non zero it will return True.

print()
print("**** np.any() ****")
print(arr)
print(np.any(arr))

arr[0,:] = 0
print(arr)
print(np.any(arr))



arr =  np.arange(1,11).reshape(2,5)
# np.mean()
# Compute the arithmetic mean along the specified axis.
 
    
print()
print("**** np.mean() ****")
print(arr)
print(np.mean(arr))
print()
print(np.mean(arr,  axis = 0)) # axis = 0  column wise 
print()
print(np.mean(arr, axis =1))  # axis = 0  row wise 

# np.std()

# np.log()

