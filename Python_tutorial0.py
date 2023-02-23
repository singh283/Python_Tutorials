#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python Implementation

CPython
Jpython
Iron Python
Ruby Python
PyPy -- Thonny Editor  
Anaconda Python 


# In[ ]:


#Extensibility  -  can run code written in  other PL into python
#Embedded - can run python code in other PL  


# # Python Components 
#      Expressions and Statements 
#      Block and Indentation
#      Comments
#      Escape sequence
#      Data Types
#      Operators

# In[ ]:


#  Expression is a combination of literals and identifiers which gives result after  execution 
#  Statements is a combination of literals and identifiers which does not gives result after  execution 


# In[1]:


# Block - if , else , elif ,  for , with , while ,  def ,  class,  try, except ,  finally 


# In[2]:


# Escape sequence 


# In[3]:


print('This 
is 
Python ')
      
# in case of multi line string the quotes is not working so here we can use '\'  to avoid the error


# In[5]:


print('This is Python ')


# In[6]:


# Datatypes : 
# Fundamental data types - int , string , float , boolean , complex 
# Derived Datatypes - list ,  Tuples ,  dictionary ,  set ,range 


# # taking input from user 

# In[11]:


num1 = eval(input('enter first no: '))
num2 = eval(input('enter second no: '))
print(num1 + num2)


# In[21]:


# input function converts everything to string so we have to typecast it in  order to  perform any mathematical function .
# eval('expr') -  function 

a = eval('10+20')
print(a , type(a))

res = list('Python')
print(res)

res = list('[10,20,30,40]') 
print(res, type(res))

# each elements of the string becomes the individual element of the list. 
# but our expectation is to get the result as [10,20,30,40] so we will use eval function 
# to evaluate the given string which is a list to its core type (list) and not as a string 

res = eval('[10,20,30,40]')
print(res, type(res))


# In[25]:


# Print FUNCTION  

# sep , end

print(10,20,30,40,50)

print(10,20,30,40,50, sep =',') 
print('one', 'two', 'three' , sep =':') 


# In[27]:


print(10)
print(20)
print(30)
print(40)


# In[30]:


# in above print statement we are getting the results in new line because by default in every print function there is 
# 'end' attribute  which is set to \n 
print(10, end = '\n')
print(20, end = '\n')
print(30, end = '\n')
print(40, end = '\n')

print(10, end = ' ')
print(20, end = ' ')
print(30, end = ' ')
print(40, end = ' ')


# In[32]:


# Output formatting 

val1 = eval(input('enter the first no: '))
val2 = eval(input('enter the second no: '))
print(f'The sum of {val1} and {val2} is {val1 + val2}')


# In[ ]:


# Operators 
    1. Arithmetic - +, -, *, /(Float division),//(Floor Division), %(Modulo Operation), ** (Exponent)
    2. Comparison >, < ,>= ,<= 
    3. Logical   and or not 
    4. Equality  ==
    5. Bitwise   & (and), |(or), ^ (xor), ~ (negation) , <<(Left shift) , >> (right shift)
    6. Assignment  = 
    7. Compound assignment  += , -= , *= , /=, //=,%= , **= , &=, !=, ^=, ~= , <<= , >>=
    8. Membership  in , not in 
    9. Identity   is , is not 
    10.Ternary    expr if cond else expr 
    11. Operator Precedence 


# In[12]:


# 1. Arithmetic - +, -, *, /(Float division),//(Floor Division), %(Modulo Operation), ** (Exponent)

print(10/3)   # Float Division  - the division operation happens until the capacity of a float number
print(10//3)  # Floor Division  -  quotient without decimal part
print(10%3)   # Modulo -  remainder 

a = 10/3
print(a , type(a))

b = 10.0/3
print(b , type(b))

# ceil value - highest nearest whole value 
# floor value - lowest  nearest whole value 

import math as m
print(m.floor(9.0009))  
print(m.ceil(9.0009))

print(10**3)
print(pow(10,3 ))



# In[7]:


# Concatenation '+'  Sequence Type
# both operand should be of same seq type 
# Concatenation operation  creates a new object 

print('String Concat --> ' , 'Learn'+'Python')
print('List Concat --> ' , [10,20,30,40] + [10,20,30,40])
print('Tuple Concat --> ' , (10,20,30,40) + (10,20,30,40))


str1 = 'Learn'
str2 = 'Python'
print(str1 + str2)
print(str1)
print(str2)


# In[5]:


# Repetition  '*'  Sequence type
# One operand should be sequence and other should be int , takes only int 
# this also creates a new object 

print('python' * 3 )
#print('python' * 3.0 ) -- can't multiply sequence by non-int of type 'float' 
#print('python' * 'python') -- can't multiply sequence by non-int of type 'str' 


# In[20]:


# Comparison Operator - <, <= , > , >=
# Return Boolean values 
# It works with only similar data types except int and float 

print(10 < 20)
print(1 < 3.0)
print(3.1 < 3.3)
#print( 30 < 30 + 0j)  error  should be of same datatype
#print('python' < 30)  error  should be of same datatype 
 # element by element comparison in case of string 
print('python' < 'python')
print('Python' < 'python')
print('Python' < 'Pythons')
print('Pythons1' < 'Pythons')  
print('10' < '9') # 10 is not less than 9 but since in string we do element by element comparison and 1 comes before 9 
# or we can say 1 is less than 9 so Overall result is TRUE 

print('10' < '00')

print(10<20<30>3<=3>=1) # In this combined expression if all conditions are True then only overall result is True,
#  if any of the conditions evalutes to be False , whole overall result will be false .



# In[30]:


#Equality Operator == , !=  
# returns boolean  value True or False 
# It compares the content 
# It works with different datatypes  

print(10 == 20)
print('A' == 65 )  
print('Python' == 'python')
print('Python' == 'Python')

print(10 ==10!= 20!=20) # if any of the condition is False then overall result will become False


# In[ ]:


#Logical Operator  and , or ,  not 
#They work with  logic and logic should always be evaluated as True or False 

# and Truth table (gives importance to False value , if any value is False the result will be False )
#True and True = True
#True and False = False
#False and True = False
#False and False = True 

# or Truth table (gives importance to True value , if any value is True the result will be True )
#True or True = True
#True or False = True
#False or True = True
#False or False = False 

# not Truth table 
# not True = False 
# not False = True




