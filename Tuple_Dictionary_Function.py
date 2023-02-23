#!/usr/bin/env python
# coding: utf-8

# In[2]:


# x = [1,2]
# y = [10, 100]

# for i in x:
#     for j in y:
#         if i % 2 == 0:
#             print(i*j)
#         print(i)
#         break
#     print(j)


# In[ ]:


# Tuple - uses small brackets ()
# Tuple is a collection of  heterogeneous elements 
# elements are seperated by comma
# Tuple is immutable 
# Tuple is  a seq 
     # Indexing , slicing , concatenation , Repetition 
     # supports  -ve and +ve indexing 

# Tuple can have DUPLICATE elements 


# In[18]:


#  Different ways of creating a Tuple 

# tpl = (10 , 10.20 , 10 + 20j , 'Python' , True , None , [1,2,3] , (1,2,3))
# print(tpl , type(tpl))

# tpl = 10 , 10.20 , 10 + 20j , 'Python' , True , None , [1,2,3] , (1,2,3)
# print(tpl , type(tpl))

# creating  a tuple with single element 
# tpl = 10 ,
# print(tpl , type(tpl))

# creating  a tuple using tuple() - tuple function takes only 1 arg

# tpl = tuple('Python')
# print(tpl , type(tpl))  #  passing  a string to tuple function returns tuple with each element in the string as individual 
                        #  element of the tuple , same as in case of list   

# tpl = tuple((10, 20 ,30 , 40))  #  passing tuple inside a tuple()
# print(tpl , type(tpl))

# tpl = tuple([10, 20 ,30 , 40]) #  passing list inside a tuple()
# print(tpl , type(tpl))

# tpl = tuple({1:100 , 2:200 , 3:300 , 4:400})  #  passing dict inside a tuple()
# print(tpl , type(tpl))

#  taking tuple as input from user 

# user_input =  eval(input('enter the tuple:  '))
# print(user_input , type(user_input))


# In[19]:


#  Immutability of Tuple 

# 1. Item assignment is not possible 
# 2. changes will not be done in same object 

# tpl = (10 , 10.20 , 10 + 20j , 'Python' , True , None , [1,2,3] , (1,2,3))
# tpl[2] = 'amit'


# In[21]:


# Tuple Packing - Assigning multiple values to a single variable 

# a = 10,20,30,40,50
# print(a , type(a))


# emp_name = 'amit'
# emp_dept = 'IT'

# emp_details = emp_name , emp_dept
# print(emp_details , type(emp_details))


# In[22]:


# Tuple Unpacking 
# No of elements inside the tuple and the no of variables should MATCH

# e_name , e_dept =  emp_details 
# print(e_name)
# print(e_dept)


# In[26]:


# List Unpacking

# lst = [10,20,30,40,50]
# a , b, c, d, e = lst
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# Unpacking can be applied to any sequence 


# In[32]:


# Tuple Methods 
# print(dir(tpl))

# count , index 

# tpl = (10, 20, 34, 50, 56 , 60, 100, 302 , 99, 33, 44, 55, 20)
# print(tpl.count(20))

# print(tpl.index(50))


# In[47]:


#  Concatenating tuple to a tuple 

# tpl =  10,20,30, 40
# tpl +=  111,

# print(tpl)

# Specifically Tuple only has 2  methods , but if we want to perform any operation on Tuple we can convert the tuple to LIST
# and after doing the operation again convert the list back to TUPLE.

# lst =  list(tpl)
# lst.append(222)
# print(lst ,type(lst))

# tpl = tuple(lst)
# print(tpl)


# In[54]:


# Dictionary - data structure to store Structured data ,
# It is a collection of key:value pair , elements are seperated by comma
# It is not a sequence like STRING , TUPLE  , LIST , so cannot perform Indexing , Slicing , concatenation , Repetition

# Can access the values using Keys 
# Dictionary is mutabale 
# key should be immutable and value should be mutable .

# emp_name = 'amit'
# emp_dept = 'IT'
# emp_address = 'bangalore'


# emp_dict =  {'emp_name':'amit', 'emp_dept':'IT' , 'emp_address':'bangalore'}
# print(emp_dict, type(emp_dict))
# print(emp_dict['emp_name'])

# for i in emp_dict:
#     print(i)
    


# In[59]:


# Dictionary is mutabale 
# key should be immutable and value should be mutable .

# d = {1:100, 2:200 , [1,2,3]:(1,2,3) }
# print(d)

# above statement will give ValueError because here key is mutuable (list is used as key)

# d = {1:100, 2:200 , [1,2,3]:(1,2,3) }
# print(d)

# keys cannot be duplicated in dictionary 

# d = {1:100, 2:200 , 20+30j:900 ,  True:None ,  (1,2,3):[100,101,100] , 'P':'Python'}
# print(d)

#  Above we can find that in the output dict  1 is having value as None because keys 1 and True are same and the later
# value replaces the previous value .


# In[55]:


print(dir(dict))


# In[71]:


# Few built-in Functions :

#  zip(iter_1, iter_2, iter_3 ..... iter_n)
# It returns a iterable object  

# lst1= list(zip('Python' , [10,20,30,40,50,60] , (100,101,102,103,104,105)))
# print(lst1)

# In case the iterables have unequal no of elements then the zip will result in the no of tuples equal  to 
# no of elements in the iterable which has lowest no of elements

# lst1 = list(zip('Python' , [10,20,30,40,50] , (100,101,102,103)))
# print(lst1)


# enumerate(iterable) - creates a list of tuples each having 2 elements 
#                              (one is the index and other is the value at that index)
# It returns a iterable object  

# list(enumerate('Python'))

# reversed(iterbale) - returns a iterable object 

# print(list(reversed('Python')))
# print(list(reversed(['Python', 'CLass'])))

# sorted(iterable) - It returns a list where each  element of the iterable is in sorted order 

# sorted('Python')


# In[80]:


# Creating a dictionary 

# d = eval(input('enter the dictionary: '))
# print(d)

# Using dict() 

# d =  dict(enumerate('Python'))
# print(d , type(d))

# dict([ele[::-1] for ele in enumerate('Python')])


# d = dict([(1,100), (2,200), (3,300), (4,400)]) - passing list of tuples inside dict()
# print(d , type(d))


# In[105]:


# Updating the dict

# emp_lst = 'Amit', 'IT' , 'Bangalore'
# emp_key = ['emp_name' , 'emp_dept' , 'emp_loc']

# emp_det = dict(zip(emp_key , emp_lst))
# print(emp_det, id(emp_det))
# emp_det['emp_loc'] = 'Delhi'
# print(emp_det , id(emp_det) )

# emp_det['emp_skill'] = 'Python'
# print(emp_det , id(emp_det) )

# # Accessing elements  from  dict 

# print(emp_det['emp_name'], emp_det['emp_skill'] , sep ='\n')

# emp_det['emp_dob'] # this will give KeyError


# In[ ]:


# print(dir(dict))

# dict methods: 

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'


# In[101]:


# get(key) - it returns the associated value if the key is present else it returns None if key is not present
# get(key,value) - it returns the associated value if the key is present else it returns the value if key is not present

# print(emp_det)
# print(emp_det.get('emp_skill'))
# print(emp_det.get('emp_city'))
# print(emp_det.get('emp_city', 'key does not exists'))

# print(emp_det)


# In[104]:


# setdefault(key) - it returns the associated value if the key is present else it returns None if key is not present
      # and updates the dictionary with  key:None 
# setdefault(key,value) - it returns the associated value if the key is present else it returns the value if key is not present
    # and updates the dictionary with  key:Value 
    
    
# print(emp_det)
# print(emp_det.setdefault('emp_skill'))
# print(emp_det.setdefault('emp_city'))
# print(emp_det.setdefault('emp_pin', '560006'))

# print(emp_det)


# In[106]:


# lst = [10,20,30,40]
# print(lst , id(lst))
# tpl = (10,20,30,40)
# print(tpl , id(tpl))

# lst = tpl  
# print(lst , id(lst))


# In[107]:


# lst = [10,20,30,40]
# print(lst , id(lst))
# tpl = (10,20,30,40)
# print(tpl , id(tpl))

# tpl = lst 
# print(lst , id(lst))


# In[110]:


# update  - similar to extend method of list 

# emp_lst = 'Amit', 'IT' , 'Bangalore'
# emp_key = ['emp_name' , 'emp_dept' , 'emp_loc']

# emp_det = dict(zip(emp_key , emp_lst))

# print(emp_det , type(emp_det), id(emp_dept))

# emp_info = {'emp_state':'karnataka', 'emp_pin':'560076'}

# emp_det.update(emp_info)

# print(emp_det , type(emp_det), id(emp_dept))


# In[113]:


# fromkeys(iterable , default =None)
# Creates a dictionary where elements of iterable will be the key and default is set as value for each key 

# d = {}
# d = d.fromkeys('Python')
# print(d)

# d = d.fromkeys('Python', 10)
# print(d)


# In[120]:


# pop ,  popitem

# pop(k) - If key is available it removes the key value pair from the dictionary else if key not present then gives key error
# pop(k,v) - If the key is available it removes the key value pair from the dictionary else it gives v as output

# print(emp_det)
# emp_det.pop('emp_state') 

# print(emp_det)

# emp_det.pop('emp_state', 'key does not exist') 


# In[121]:


# popitem() -  removes the last entry from the dict
# emp_det.popitem()
# print(emp_det)


# In[131]:


# items, keys, values 

# print(emp_det)

# print(emp_det.keys())

# print(list(emp_det.keys()))

# print(list(emp_det.values()))

# print(list(emp_det.items()))


# In[134]:


# clear - removes all the elements from dict 

# emp_det.clear()

# emp_det


# In[18]:


# Dictionary Comprehension 

# {key:value for ele in iterable}

# email_lst = ['aksingh283@gmail.com' , 'ashish_kumar@gmail.com',  'ravi@hotmail.com',  'sid@redifmail.com']

# d = {i[:i.index('@')+1]:i[i.index('@')+1:i.index('.')] for i in email_lst }

# print(d)


# d1 = {email_lst[ele][:email_lst[ele].index('@')+1]: email_lst[ele][email_lst[ele].index('@')+1:email_lst[ele].index('.')] for ele in range(4) }

# print(d1)


# In[1]:





# In[10]:


# lst = [10,20,30,40]
# lst1 = lst 

# print(lst)
# print(lst1)

# print(lst == lst1)

# print(id(lst))
# print(id(lst1))

# print(lst is lst1)

# Shallow copy and Deep Copy 
# applicable for mutable objects and not for immutable objects 
# print('****** Shallow Copy Example *****')

# Shallow Copy  -  slicing ,  copy 

# lst_s = [10,20,30,40]
# lst_s1 = lst_s[::] 


# print(lst_s)
# print(lst_s1)

# print(lst_s == lst_s1)


# print(id(lst_s))
# print(id(lst_s1))


# print(lst_s is lst_s1)

# lst_s1[0] = 111

# print(lst_s)
# print(lst_s1)

#  in case we have nested list then during shallow copy both points to same object (nested list), so changes in nested list
# will have impact in both the orignal and the shallow copy created  .

# lst = [10,20,30 ,[100,200,300]]
# lst3 = lst[::]

# print(lst , id(lst))
# print(lst3, id(lst3))

# Above we have created a shallow copy lst3 of lst .  
# NOW since lst is having a nested list and if we make any changes to the nested list it will be reflected in shallow copy
# as well because both lst and lst3 shares the sames nested object.

# print(id(lst[-1])) 
# print(id(lst3[-1])) 

# lst[-1][0] = 101

# print(lst , id(lst))
# print(lst3, id(lst3))

# To  solve the above issues we have "Deep Copy" , making changes to the nested object  will not have impact on the copy or 
# vice - versa

# from copy import  deepcopy

# lst = [10,20,30 ,[100,200,300]]
# lst4 = deepcopy(lst)

# lst4[-1][1] = 222
# print(lst)
# print(lst4)

# print(id(lst[-1]))
# print(id(lst4[-1]))


# In[11]:


# Functions : 
# functions - advantage is code reusability 

# built-in functions -  len, float 
# user defined 

#syntax 

def func_name(param):
    ''' documentation '''
    code
    code
    code
    return ret_val

# example

def my_func():
    ''' This is my_function '''
    

my_func()

# to access the documenation

print(my_func.__doc__)


# In[12]:


# def my_func(a,b,c):
#     print(a)
#     print(b)
#     print(c)
    
# my_func(10,20,30)

# Argumnets are actual values 
# Parameters are variables that stores the arguments.


# In[ ]:


# Types of Parameters : 
    1. Postional Parmeters 
    2. defualt parameters 
    3. keyworded arguments 
    4. Variable length positional arguments  - *args
    5. Variable length keyworded arguments  -  **kwargs 
    


# In[19]:


# 1. Positional Parameters
    # order is important 
    # no of arguments and parameter should match 
    
# To filter out the emails where length of user name is more than 10 

# lst = ['aksingh283@gmail.com' , 'ashish_kumar@gmail.com',  'ravi@hotmail.com',  'sid@redifmail.com']

# def lst_func(lst , len_usr_name):
#     for email in lst:
#         if len(email[:email.index('@')]) > len_usr_name :
#             print(email)
            
# lst_func(lst , 10 )


# In[31]:


# 2. Defualt Parameter
# Defualt Parameter should always follow the positional parameter .

# def my_func(lst , no_of_times = 3 ,  terminating_val = '#'):
#     for i in lst:
#             if i.isnumeric():
#                 print(i*no_of_times)
#             else:
#                 print(i + terminating_val)
            
# my_func(['41', 'Dragon' , '10', 'star'])
# my_func(['41', 'Dragon' , '10', 'star'], 5 , '$')


# In[35]:


# 3. keyworded arguments

# def my_func(lst , no_of_times = 3 ,  terminating_val = '#'):
#     for i in lst:
#             if i.isnumeric():
#                 print(i*no_of_times)
#             else:
#                 print(i + terminating_val)
            
# my_func(['41', 'Dragon' , '10', 'star'])
# my_func(['41', 'Dragon' , '10', 'star'] , terminating_val = '$') 

# above we are skipping one of the default Parameters so in case whenever we skip any of the defualt paramters we should 
# be using keyworded argument  


# my_func( terminating_val = '$',  ['41', 'Dragon' , '10', 'star'] ) 

# BUT ALSO need to remeber that if we are using a MIX of postional and keyworded argument then  keyworded argument
# should always come after positional argument  . 


# In[40]:


# 3. Variable  length positional argument   *args
# *args internally is a TUPLE 

# def fun(a,b, *arg):
#     print(arg , type(arg))
#     print(a+b+sum(arg))

# fun(10,20, 30,40,50)


# def fun(a,b, *arg , c = 111): # here arg is taking 30 , 40, 50 and default value is coming for 'c'
#     print(arg , type(arg))
#     print(a+b+sum(arg))
#     print(c)

# fun(10,20, 30,40,50)


# def fun(a,b, *arg , c = 111): # here arg is taking 30 , 40 and if we want some explicit value for default param 'c'
#     print(arg , type(arg))    # then we need to pass it as keyworded argument 
#     print(a+b+sum(arg))
#     print(c)

# fun(10,20, 30,40,c= 50)


# def fun(a,b,  c = 111, *arg ):   # here *arg is taking the left over values 40  and 50 as 30 is considered as value for 'c'
#     print(arg , type(arg))
#     print(a+b+sum(arg))
#     print(c)
    
# fun(10,20, 30,40,50)


# In[45]:


# 4. Variable length keyworded argument  **kwargs 
# **kwargs internally is a DICT  

# def emp_details(e_name , e_id , e_sal , *args , **kwargs):
#     print(kwargs , type(kwargs))
#     print(args , type(args))
#     print(e_name)
#     print(e_id)
#     print(e_sal)

# emp_details('Amit' , 3333 , 100000 )

# emp_details('Amit' , 3333 , 100000 , e_city = 'Bengaluru' , e_state = 'Karnataka')


# In[53]:


# Namespace - Container 
    # Built-in 
    # Global
    # Local

    
# def my_func():
#     a = 10
#     b =20
#     def inner_func():
#         a = 11
#         b = 21
#         print(a ,b)
#     inner_func()
#     print(a,b)


# my_func()

# print('==================\n\n\n')

# def my_func():
#     a = 10
#     b =20
#     def inner_func():
#         nonlocal a   # this is used in case  of inner and outer variables.
#         a = 11
#         b = 21
#         print(a ,b)
#     inner_func()
#     print(a,b)


# my_func()


# In[57]:


# global keyword 

# a = 10
# b = 20

# def f1():
#     global a  
#     a = 11
#     b = 21
#     print(a,b)
# f1()
# print(a,b)


# In[58]:


# Function reference 

# def f1():
#     a = 10
#     b = 20
#     print(a , b)
    
#f1()
# f1  # this will give information that there is function f1() under main namespace , in order  to call the function it requires 
    # () with function name 


# In[65]:


# Closure

# def f1():
#     a =10
#     b =20
#     return a ,b 

# f2 = f1      #  Here f1 is refernce to function object f1() , so as f2 =f1 same reference will be assgined to f2  
# print(f2)
# print(f1)

# f2()        # Now since f2 = f1 , f2 also pointing to same reference as f1 which is the function object so using f2() 
            # we can call the function object 
    

#  Calling the inner function in outside / Global namespace - this is called Closure 

# def f1():
#     def inner():
#         a =10
#         b =20
#         print('Inside inner function ')
#     return inner
    
# i1 =  f1()   # here function call is returning reference of inner() which is then assigned to variable i1 ,  and now we 
                # use that i1 variable to directly call the inner() as it has its reference .
# i1()
    


# In[70]:


# lst =  list(range(11,20))

# def even_odd(num):
#     return True if num%2 == 0 else False 


# def my_func(func, lst):
#     out_lst = []
#     for ele in  lst:
#         if func(ele) :
#             out_lst.append(ele)
#     return out_lst

# my_func(even_odd , lst)


# In[74]:


# %timeit my_func(even_odd , lst)

# "timeit" is a method of measuring the execution time of your python code snippets.


# In[77]:


# Lambda function / Anonymous function 
# Using lambda keyword
# Syntax lambda parm:expr 
# Expr result is the return value , don't have to write the return explicitly

# (lambda num : True if num%2 == 0 else False)(4)

# a = (lambda num1 , num2 , num3 : num1 if ((num1>num2) and (num1>num3)) else num2 if num2>num3 else num3)(10,12,13)
# print(a)


# In[90]:


# Filter: - used to filter a seq based on some condition 
# Syntax -  filter(func , seq/iterable )
# Returns a filter object  - which is an iterator
# In case of filter the variable (num) which  satisfied the condition got added to the result set.


# list(filter(even_odd , lst ))

# tuple(filter(lambda num: num%2 ==0 , lst ))


# In[106]:


#  Map - used to map object from one seq to another seq 
# Syntax -  map(func, iterable)
#  returns map object - which is an iterator
# In case of map the result of the expression got added to the result set.

# print(lst)
# list(map(lambda num: num%2 ==0 , lst))


# In[112]:


lst_email = ['amit@gmail.com' , 'rohitkumar@yahoomail.com' , 'raghuram@rediffmail.com', 'krishna@hotmail.com', 
            'manoj@gmail.com']

# filter the list and return a list of email where username > 5
# list(filter(lambda lst_email : len(lst_email[:lst_email.index('@')]) > 5 , lst_email))

# filter the list and return a list of username for only those email id where username > 5
# list(map(lambda email: email[:email.index('@')] , filter(lambda lst_email : len(lst_email[:lst_email.index('@')]) > 5 , lst_email)))


# In[114]:


# sort()
   
# lst = [(10,1) , (100,2) , (23,90) , (99, 9) , (87, 7) , (67, 6) , (54,5)]

# lst.sort(key = lambda tpl:tpl[-1])

# lst


# In[116]:


# reduce -  used to find aggregate values - sum , min, max , avg  
# import reduce from functools 
# reduce(func,  seq)
# returns one single aggregate value 

# from functools import reduce 
# lst =  list(range(11,20))

# reduce(lambda x,y : x+y , lst )


# In[117]:


print(dir(__builtins__))


# In[119]:


# Iterators & Generators

#  Container Type/ Iterable -  list  , tuple , set ,  frozenset  ,  dictionary , byte , bytearray

# print(dir(list))


# In[15]:


# Iterable  -  object which implements __iter__ function 

# lst = [10,20,30,40]

# print(next(lst))  # this will give error as lst is not an Iterator , it is an Iterable object 

# lst = iter(lst)  #  here we convert the list to an Iterator object so that we can traverse the list elements using __next__
                 # function
    
# print(dir(lst))   # so the lst is converted to Iterator object as we can now see it implements both __iter__ and __next__
                  # function 

# print(next(lst) , next(lst) , next(lst) , next(lst) ) 


# In[9]:


# Iterator -  object  which allows iteration over container or Iterabale object 

# Iterator - implements __iter__ and __next__ function 

# zip , enumerate , reversed, filter , map 

# print(dir(enumerate))   # enumerate is an Iterator as it implements both __iter__ and __next__ function 

# a = enumerate('Python')

# print(next(a) , next(a) , next(a), next(a) , next(a), next(a))

# print(next(a) , next(a) , next(a), next(a) , next(a), next(a) , next(a)) # here we are exceeding the no of elemnets in the 
                                                                      # Iterable object so getting StopIteration error


# In[18]:


lst = [10,20,30,40]

for i in lst:
    print(i) 


# In[33]:


# Generator  
# Syntax of defining Generator is similar to defining a function 

# In case of generator we use yield 

# yield keyword is similar to return statement

# used to  define user defined seq 

# It is effecient in terms of memory and speed both

# import sys
# lst =  [i for i in range(10000)]
# # print(lst)
# print(sys.getsizeof(lst))

# here above it is going to give all the values upto 10000 at a  time consuming lots of memory - 85176 bytes 

# samething can be done using tuple comprehension , but tuple comprehension does not generate the tuple object
# instead it generates the Generator object

# tpl = (i for i in range(10000))
# print(tpl)
# print(sys.getsizeof(tpl))

# here above we can see that all the values are not generated at once rather it creates a generator object 
# which when used with next function starts fetching those values .
# So it does not require huge amount of memory for storing all the values at once .

# Generator object is also an Iterator  object 

# print(dir(tpl))
# print(next(tpl))


def my_gen():
    a =10
    b =20
    c =a+b
    yield 10
    yield 10.20
    yield 10+20j
    yield 'Python'
    yield [1,2,3]
    yield True

g = my_gen()

for i in g:
    print(i)


# In[37]:


# Modules in Python
# Any python file(.py)  is a module 

print(dir())  #  Global namespace 

import math
print()
print(dir())  # after  import we can see math is added to our Global namespace

print(dir(math))

math.sqrt(4)


# In[3]:


# ALternate way to import math module 

print(dir())

import math as m    #  math module is renamed as  m 

print()

print(dir())  

print(m.sqrt(4))
print(math.sqrt(4)) # this will give error as there is no such module named as "math" in global namespace


# In[4]:


print(dir())

from math import *   #  imports all functions for math module 

print()

print(dir())


# In[1]:


from math import sqrt , log  

print(dir())


# In[ ]:




