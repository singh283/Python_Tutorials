#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Logical Operators Continue ... 

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

year = int(input('Enter the year: '))
if (( (year%4==0 ) and (year%100 ==0) and (year%400 == 0)) or ((year%4==0 ) and (year%100 != 0))):
    print('leap year')
else:
    print('not leap year')


# In[ ]:


# If A and B are not Boolean datatype then 

# A and B => result is A , if A is False else result is B  (in case of and False value is given priority)
# A or B => result is A , if A is True else result is B  (in case of or True value is given priority)


# In[11]:


# Boolean - True . False 
# True => 1 
# False => 0 

# Int - 0 is always False ,rest all values are  True
# Float - 0.0 is always False ,rest all values are  True
# Complex - 0 + 0j is always False ,rest all values are  True
# string - '' is always False ,rest all values are  True
# None is always False 
# List,  Tuple , dict , Set - [] , () , {} , Set() is always False, these data structures with at least one element are True.

print(bool(''))
print(bool([]))
print(bool({}))
print(bool(' '))
print(bool([1]))
print(bool({1}))

print(10 and 20)
print(10 or 20)

print(0 and 0.0) # when we pass values with Boolean Operator we get values .
print(0 or 0.0)

print(bool(''))
print(bool([]))
print(bool({}))


# In[30]:


# Bitwise Operator (Binary Operator) - & ,| ,^ , ~ , << , >> 
# works on bit or binary values  
# Bitwse and - &  equivalent to *
# Bitwise or  | equivalent to + 
# Bitwise ^  equivalent to (A+B)(A'+B')
# Bitwise ~n equivalent to -(n+1)
# Bitwise num << by no of bits equivalent to num*(2**no of bits)
# Bitwise num >> by no of bits equivalent to num//(2**no of bits)

# print(37 & 57) => 33

print(bin(37))   # 100101  
print(bin(57))   # 111001

#  100101 *  111001  =   100001  ( here we are doing normal multiplication)

# print(37 ^ 57) => 28


# print(37 | 57)  => 61 

#---------------------
# 37 => 100101 
# 57 => 111001 
#---------------------
# & => 100001
# | => 111101
# ~ => 011100
#-------------------

# print(0b100001) => 33
# print(0b111101)  => 61
# print(0b011100) => 28
 
# A = 0
# A' = 1
# A' = 1 
# A = 0 


# In[32]:


# Bitwise Negation ~ 
# ~num =  -(num+1)

print(~9)
print(~-8)


# In[36]:


# Bitwise LFET SHIFT <<  and >> RIGHT SHIFT

# print(165 << 9)

# print(165(2**9)*)


# In[ ]:


#  Assignment Operator  =

# var1 = 'amit'

# var2 = 'sumit'

# class Employee:
#    def __init__(self , e_name , e_id):
#         self.emp_name = e_name
#         self.emp_id = e_id 


# In[37]:


# Compound Assoignment Operation - += , -= , *= , /=, //= , **= , %== , &= ,|==, ^== , ~==, <<== , >>=

# a =10
# a += 2      a = a+2
# print(a)


# In[43]:


# Membership Operation -  in , not in 
# Always return Boolena values 

# Iterables - string , List, Tuple ,  dict, Set 
# Iterator Types - enumerate , zip ,  filter , map 


# my_str = 'peter piper picked a peck of pickled peppers'
# my_lst = [1, 2, 3, 4, 5]
# my_tpl = (10,20,30 ,40)
# my_dict = {'name':'amit', 'age':30}

# print('p' in my_str)
# print('peter piper' in my_str)
# print('peterpiper' in my_str)

# print(5 in my_lst)

# print(50 in my_tpl)
# print('age' in my_dict)
# print(30 in my_dict)


# In[53]:


# e = enumerate('Python')
# print(e, type(e))

# print(list(e))

# print((0,'P') in e)


# In[55]:


# a = 'Python'
# b = 'Python'
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)   # memory address is same so result is True
# print(id(a))


# In[ ]:


# why for below example getting different memory  address
# INTEGER  CACHING 
# STRING INTERNING
     # By using intern you ensure that you never create two string objects that have the same value 
     #  - when you request the creation of a second string object with the same value as an existing string object, 
     #   you receive a reference to the pre-existing string object. This way, you are saving memory.
     #  String Interning is a process of storing only one copy of each distinct string value in memory.
# OBJECT REUSABLITY 


# In[54]:


# a = 'Python class' 
# b = 'Python class'
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)   # memory address is different so result is False , because here in this case both variables a and b are 
                  # pointing to two different memory location , here String Intering is not applied may be because of diff 
                  # version of python .
# print(id(a))


# In[61]:


# Ternary Operator  - expr1 if condn else expr2
# expr1 if condn1 else expr2 if cond2 else expr3
# We cannot use Ternary  Operator if we have multiple expresions(expr) for a given condn .

# Python Ternary operator is used to select one of the two values based on a condition, it is a miniature of if-else statement
# however here we can write the code in sinlge line.

# Greatest Of two nos .
# first_no = int(input('enter the first no: '))
# sec_no = int(input('enter the sec no: '))
# print(f'Greatest of two nos is : ', first_no if first_no > sec_no else sec_no )


# In[ ]:


# Operator Precedence 

# Operator*Meaning
# ()                 ---                     


# In[62]:


print(complex(True))


# In[71]:


# Strings in Python  - '...' , "...." , '''....''' , """...."""

# my_str =  """Amit"""
# print(my_str , type(my_str))

# print('This is Python\'s class')
# print("This is Python's class")

# my_str = 'This is Python"s class'
# print(my_str , type(my_str))

# my_str = '''This is Python"s clas's'''   # in case we have " as well as ' in the string use '''...'''
# print(my_str , type(my_str))

# my_str = """This is Python"s clas's"""  # in case we have " as well as ' in the string use """...."""
# print(my_str , type(my_str))

# To write multi line string we use '''...'''
# my_str= '''This 
# is
# Python's
# class'''
# print(my_str , type(my_str))

# To write the documentation 

# def f1():
#     '''This is documentation for f1'''
#     return 10

# f1()
# print(f1.__doc__)


# In[95]:


# How string is stored in memory 
 # At individual element level 
 # Whole string object level 

# String supports +ve as well as -ve index
  #   +ve index starts from 0 from LHS    step => +ve
  #   -ve index starts from -1 from RHS   step => -ve (this is mandatory while Slicing in reverse direction)

# Indexing , Slicing , Concatenation , repetition

#Indexing -  Accessing one element at  at time.

my_str = 'This is Python class'
# print(my_str[0])
# print(my_str[-len(my_str)])

# print(my_str[19])
# print(my_str[-1])
# print(my_str[len(my_str)-1])


#Slicing -  Accessing multiple elements at  at time.
# string[start_index : stop_index+1 : step]

print(my_str[8:14])  
print(my_str[8:14:2])  

print(my_str[-7:-13])  
print(my_str[-7:-13:1])  
  
print(my_str[-7:-13:-1])

print(my_str[::2])
print(my_str[::-2])

# Default step = 1
# Default start = 0 , stop = len(my_str), step = +ve
# Default start = -1 , stop = -len(my_str)-1, step = -ve
# 'This is Python class'

print(my_str[::])
print(my_str[::-1])


# In[99]:


# String Concatenation '+' 
# Both operands should be string 

# print('Python' + 'class')
# print('Python' + 1) # ERROR - can only concatenate str (not "int") to str 


# In[101]:


# String Repetition * 
#  One Operand should be string and another should be int 

# print('Python' * 3)
# print('Python' * 3.0) # ERROR - can't multiply sequence by non-int of type 'float' 


# In[102]:


# String Methods 

# print(dir(str))

# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
# 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'


# __xxx__ - these are called  'Magic Methods'/ Dunder internally used by Python for doing operation , 
# like when we do add operation '+' two  add two nos, then Python interanally calls __add__ method . 

# '__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
# '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__'


# In[116]:


# 'capitalize', 'casefold', title , swapcase 

# my_str = 'peter piper picked a peck of pickled peppers'
# print(my_str.capitalize())  # Capitalize first letter of the string 
# print(my_str.title())       # Capitalize first letter of each word of the string 

# print(my_str.swapcase())

# print(my_str.lower())
# print(my_str.casefold())     # casefold method does same thing as lower method but is more aggresive 

# my_str = 'fließen'
# print(my_str.lower())  
# print(my_str.casefold())      # wherever we are expecting the input to be not in ASCII character there we can use 
                              # casefold() to convert the non-ASCII character to its lower case ASCII  equivalent
    
    
# startswith 
my_str = 'peter piper picked a peck of pickled peppers'

print(my_str.startswith('p'))
print(my_str.startswith('pip'))
print(my_str.startswith('pet'))
print(my_str.startswith('p', 21, 30))

