#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Conditional statement in Python 
    # if elif else 
# Loops control in Python
    # for , while 
    # break , continue


# In[3]:


# if 1:
#     print('first if block')
# if 0:
#     print('second if block')
# else:
#     print('In Else block')

# Here if the first if condn is True python will also check other subsequent if condn and 
# "if the LAST if condn is not True then will also execute the else block corresponding to it  .
    


# In[4]:


# if 1:
#     print('first if block')
# elif 1:
#     print('second if block')
# else:
#     print('In Else block')
    
# Here if the first if condn is True python will not check other elif (even if they are True) and the else construct  .


# In[16]:


# Laep Year 

#  if year is divisible by 100 then check if it is  also divisible by 400  - True - Leap year
#  if year is divisible by 100 then check if it is not divisible by 400  - True - Not a Leap year
#  if year is divisible by 100 then check if it is also divisible by 4  - True - Leap year

# year = eval(input('Enter the year  : '))

# if year%4 == 0 :
#     if year%100 != 0:
#         print(f'{year} is a leap year')
#     elif year%100 == 0 :
#         if year%400 == 0:
#             print(f'{year} is a leap year')
#         else:
#             print(f'{year} is not a leap year')       
# else:
#     print(f'{year} is not a leap year')


# In[13]:


# year = eval(input('Enter the year  : '))

# if year%4 == 0 :
#     if year%100 == 0 :
#         if year%400 == 0:
#             print(f'{year} is a leap year')
#         else:
#             print(f'{year} is not a leap year')
#     else:
#         print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')


# In[22]:


#  WAP to check if the character input is a vowel or consonant 

# letter = eval(input('enter the letter : '))

# if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
#     print(f'{letter} is a vowel ')
# else:
#     print(f'{letter} is a consonant ')


# In[27]:


False or 'e'


# In[9]:


# Loops in Python 

# pass_store = 'Welcome123'

# user_pass = eval(input('enter the password: '))

# for i in range(0,3):
#     if i <= 2 :
#         print(f'This is {i+1} attempt ')
#         if (user_pass == pass_store):
#             print('password is correct ...')
#             break
#         else:
#             print('password is not correct !!')
#             user_pass = eval(input('enter the password: '))
#     else:
#         print('Sorry , You have exhausted all the Attempts !!') 
#         break     


# In[31]:


# Iterable - any object that implements __iter__ function 

# print(dir(str))


# In[20]:


# range(start , stop , step)
# generates a seq of nos from start to stop(exclusive) 

# start = 0 , step = 1 

#step - +ve then generates the seq of no in forward direction ----------->
#step - -ve then generates the seq of no in backward direction ----------->

# print(list(range(10)))
# print(list(range(11,20, 1)))
# print(list(range(11,20, -1)))
# print(list(range(20,11, -1)))

# my_str = 'Python'    
# print(list(range(len(my_str))))


# In[15]:


# for i in range(5):
#     print(i)
#     print(i*2)
#     print(i**2)


# In[37]:


# for i  in 'Python':
#     print(i)
#     print()

# print('=================\n')


# my_str = 'Python'    
# for i in range(len(my_str)):
#     print(i)
#     print()
#     print(my_str[i])

# print('=================\n')

# my_str = 'Python'    
# for i in range(-1 , -len(my_str)-1, -1):
#     print(i)
#     print()
#     print(my_str[i])

    
# print('=================\n')


# for i in (1,2,3,4):
#     print(i)
#     print()
    
    
# print('=================\n')


# for i in [1,2,3,4]:
#     print(i)
#     print()
    
# print('=================\n')


# for i in {1:100,2:200,3:300,4:400}:
#     print(i)
#     print()  
    
    
# print('=================\n')

# d = {1:100,2:200,3:300,4:400}
# for i in d:
#     print(i)
#     print(d[i]) 
    
    
# my_str = 'Python'    
# for i in my_str:
#     print(i)
#     print()   


# In[39]:


#Enumerate - gives index and the value at the index in 
# enumerate(iterable, start=0)
# iterable - a sequence, an iterator, or objects that supports iteration
# start – is the position in the iterator from where the counting starts.
# Default is 0.
# returns a TUPLE consisting of index and the value at that index 

# for i  in enumerate('Python'):
#     print(i, type(i))
#     print()


# In[4]:


# While loop 

# orig_pwd = 'Python123'
# user_pwd = input('enter the password: ')

# while orig_pwd != user_pwd:
#     print('The password is incorrect !!')
#     print('Re-enter the correct password ... ')
#     user_pwd = input()
# else:
#     print('The password is correct')


# In[19]:


#  Take a num as input and find the sum of it's digits

# input_num = input('enter the number: ')
# str_len = len(input_num)
# res = 0

# while str_len > 0:
    
#     res += eval(input_num[str_len -1])
#     str_len -= 1


# print(res)   


# In[37]:


# factorial of a no 

# input_num = int(input('enter the number: '))
# res = 1

# for i in range(1, input_num + 1):
#         res *= i
# print(res)  


# input_num = int(input('enter the number: '))
# res = 1

# for i in range(1, input_num + 1):
#         res *= i
# print(res)  


# In[38]:


#  Take a string from user  and reverse it using loop  

# input_str = input('enter the string : ')
# str_len = len(input_str)
# reverse_str = '' 

# while str_len > 0:
#     reverse_str += input_str[str_len-1]
#     str_len -= 1

# print(reverse_str)


# In[42]:


# continue -  skips the current iteration  

# lst =  list(range(10))

# for i in lst:
#     if i == 6:
#         continue
#     else:
#         print(i)

