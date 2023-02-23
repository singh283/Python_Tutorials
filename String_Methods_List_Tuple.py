#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Integer Caching 
# String Interning

# Object Resusability (CPython)
    # Integer => -5 to 256 
    # String => A-Z, a-z , 0-9, _
    # Boolean => True , False
    # None


# In[5]:


# String Methods:

# find() - it returns the lowest index of the fisrt occurence of the matching substring into the main string .
# IF substring is not found returns -1 

# rfind() - it returns the hihgest index of the matching substring into the main string .
# IF substring is not found returns -1 

# my_str = 'peter piper picked a peck of pickled peppers'
# print(my_str.find('p'))
# print(my_str.find('z')) 
# print(my_str.find('peck'))

# print(my_str.rfind('p'))
# print(my_str.rfind('z')) 
# print(my_str.rfind('peck'))


# In[8]:


# index() - it returns the lowest index of the fisrt occurence of the matching substring into the main string .
# IF substring is not found returns valueError

# rindex() - it returns the hihgest index of the matching substring into the main string .
# IF substring is not found returns valueError


# print(my_str.index('p'))
# print(my_str.index('z')) 
# print(my_str.index('peck'))

# print(my_str.rindex('p'))
# print(my_str.rindex('z')) 
# print(my_str.rindex('peck'))


# As mentioned above if substring NOT found find returns -1 BUT index gives "value Error"

# In[10]:


# count()

my_str = 'peter piper picked a peck of pickled peppers'
print(my_str.count('p'))
print(my_str.count('pe'))
print(my_str.count('pe', 6 , 21), my_str.count('pi', 6 , 21))


# In[18]:


# isidentifier - True is string is valid identifier else False ( Gives - True in case of keyword)
# isprintable - checks if all charatcers in a string are in printable format.

my_str = 'Peter \vpiper picked \na peck of \tpickled peppers'
print(my_str)
print(my_str.isprintable())  # since all characters are not printable \v, \n , \t 

my_str = 'Peter \\vpiper picked \\na peck of \\tpickled peppers'
print(my_str)
print(my_str.isprintable()) # now it is printable as we have use '\' character to  void there special behaviour.

import keyword
print(keyword.iskeyword('for'))



# In[27]:


# center , rjust, ljust , zfill - used for string formatting 

# my_str = 'Python'
# print(my_str.rjust(20))
# print(my_str.rjust(20, '*'))
# print(my_str.ljust(20, '+'))
# print(my_str.center(20, '*'))

# print(my_str.zfill(20))
# print(my_str.rjust(20, '0'))


# In[29]:


# strip , lstrip , rstrip -  Used to un-necessry spaces from ends of the string 

# replace - replace all the occurences of the substring from the string 

my_str = 'peter piper picked a peck of pickled peppers'

# print(my_str.replace('p' , 'z'))
# print(my_str.replace('p' , 'z', 5)) # replaces first 5  occurences  of the substring from the string


# In[35]:


# SPLIT <STRING SE LIST> , JOIN   <LIST SE STRING> 
# by default split method splits the string from spaces and returns a list.
# and the split charcter will not be included in the rseult .

my_str = 'peter piper picked a peck of pickled peppers'

# print(my_str.split())
# print(my_str.split('p'))

# lst_split = my_str.split()
# print(lst_split)

# join method takes a list as an argument and returns a string .  
# ' '.join(lst_split)
# '-->'.join(lst_split)
# ''.join(lst_split)


# In[37]:


# Partition - retruns a TUPLE of three elements 

# first element -  is from begining to the partition character or word -1
# second element - the partition character  or the word itself.
# third element  - from partition charcter or word +1 till end 

# my_str = 'peter piper picked a peck of pickled peppers'
# print(my_str.partition('a'))
# print(my_str.partition(' '))


# In[39]:


# splitlines - returns a list of elements splitted from \n

# my_str = 'peter piper picked \na peck of pickled peppers'
# print(my_str.splitlines())

# my_str = 'peter piper picked \na peck of \npickled peppers'
# print(my_str.splitlines())


# In[75]:


my_str = 'peter piper picked a peck of pickled peppers'

print(my_str[::-1])

# loop comprehension 
# out_str = [i[::-1] for i in my_str.split()]
# print(' '.join(out_str))

# print(' '.join([i[::-1] for i in my_str.split()]))


# print(' '.join([i[::-1] for i in my_str.title().split()]))

# ['-'.join(i[::-1]) for i in my_str.split()]


# In[100]:


# List - Any value kept inside []
# lst = [10, 10.20 , 10+20j , 'Python' , True , None ]
# print(lst , type(lst))

# List - Is a sequence 
    # List supprorts +ve and -ve indexing 
    # Indexing , Slicing , Concatenation , Repetition , len()
    
# List is a collection of heterogeneous data elements 
# List can have duplicate elements 
# List is mutuable type 
    # Allow the item assignment
    # changes will be done in the same object.
    

# List Creation:

# lst = [10, 10.20 , 10+20j , 'Python' , True , None ]
# print(lst , type(lst))

# using list(iterable) function :
# Iterable - is any object which implements __iter__ method 
# print(dir(list))
# print(dir(str))
# print(dir(tuple))
# print(dir(dict))

# All above are iterables as they uses __iter__ method 

# lst1 = list(input('enter the list : '))  # this will turn the string each character  into individual element of the list.
# print(lst1, type(lst1))

# so we should eval here while taking input  as a list 
# lst1 = eval(input('enter the list : '))  
# print(lst1, type(lst1))

# lst1 = list('10,20,30,40')    # string as Iterable 
# print(lst1, type(lst1), id(lst1))

# lst1 = list([10,20,30,40])   # list as Iterable 
# print(lst1, type(lst1), id(lst1))

# lst1 = list((10,20,30,40))   # tuple as Iterable 
# print(lst1, type(lst1), id(lst1))

# lst1 = list({1:100, 2:200, 3:300, 4:400})   # dict as Iterable 
# print(lst1, type(lst1))

# Creating list using list comprehension 
# [expr for var in iterable if condn]


# [ i*10 for i in range(1,5)]

# my_str = 'Python'
# [i for i in my_str]

# [i for i in {1:100, 2:200, 3:300, 4:400}]

# d = {1:100, 2:200, 3:300, 4:400}
# [d[i] for i in d]


# In[78]:


# eval - evaluates the expression  inside the quotes 

# print(eval("'am'+'it'"))
# print(eval("10+20"))


# In[106]:


# range - Is a sequqnce 
# syntax - range(start , stop , step)

# print(list(range(1,5)))
# print(list(range(12,20, 2)))
# print(list(range(12,-16, -1)))


# In[121]:


# Nested List:
#  -6.   -5.     -4.       -3.        -2.    -1.
# [10 , 10.20 , 30+40j , [1,2,3,4] , True , None]
#  1.    2.      3.       4.          5.     6.
    
    
# lst = [10 , 10.20 , 30+40j , [1,2,3,4] , True , None]
# print(lst[3][1])

# lst1 = [10, 33, 44, [52, 39 ,[23, 34, [99, 88, 77]]]]
# print(lst1[3][-1][-1][1])


# In[149]:


#  List Methods 

# print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# adding elements to the list

# Append -  adds the value to the end of the list .

# lst =  [ 10 , 10.20 , 30+40j , [1,2,3,4] , True , None]
# print('Before append ' , id(lst))
# lst.append(111)
# print('after append ' , id(lst), lst)

# extend - extends a  list  to another  list 
# it adds elements individually inside the existing list 

# lst =  [ 10 , 10.20 , 30+40j , [1,2,3,4] , True , None]
# lst1 = ['a','b','c','d']

# lst.append(lst1)
# print(lst)


# lst2 = ['a','b','c','d']
# lst.extend(lst2)

# print(lst)


# In[150]:


# insert(index ,value)

lst = [ 10 , 10.20 , 30+40j , [1,2,3,4] , True , None]
lst.insert(3, 111)
print(lst)


# In[159]:


# pop , remove , clear 

# pop() - removes the last element from  the list 
# returns index error if list is empty
# it returns the values which has been removed

# lst = [10,20,30,40]
# lst.pop()
# print(lst)

# pop(ind) - removes the element specified at the given index
# returns index error if list is empty or index does not exist
# it returns the values which has been removed

# lst = [ 10 , 10.20 , 30+40j , [1,2,3,4] , True , None]
# lst.pop(2)
# print(lst)


# remove(val) - removes the first occurence of the value specified from the list
# returns valueError if the value is not present in the list

# lst = [ 10 , 10.20 , 30+40j , [1,2,3,4] , True , None , 10]
# lst.remove(30+40j)
# print(lst)

# lst.remove(2)
# print(lst)

# lst.remove(10)
# print(lst)

# clear() - clears the list or deletes all the elements of the list
# returns empty list 

# lst = [ 10 , 10.20 , 30+40j , [1,2,3,4] , True , None , 10]
# lst.clear()
# print(lst)


# In[161]:


# count(val) -  counts the no of occurence of the value in the list

# lst = [10,20,30,  10, 40, 30,  50,60, 10]
# print(lst.count(10))

# index(val) - gives the index of the fisrt occurence of the element inside the list
# gives valueError if the value is not present in the list
# print(lst.index(30))


# In[167]:


# reverse - 

lst = [ 10 , 10.20 , 30+40j , [1,2,3,4] , True , None , 10]
lst.reverse()
print(lst)

# lst.sort()
# print(lst) # we get TypeError as  '<' not supported between instances of 'NoneType' and 'int' 

lst = [10,20,30,  10, 40, 30,  50,60, 10]
lst.sort()  #  default - ascending order sorting 
print(lst)

lst.sort(reverse = True)   #  Descending order 
print(lst)


# In[ ]:


# CORE PYTHON PROGRAMING by Nageswar Rao 

