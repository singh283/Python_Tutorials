#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Append Mode - a

# If the file exists then  it will open the file in append mode and places the cursor at the end of the file.
# If the file does not exist then it will create the file 
# In this mode we are only allowed to write and not to read from the file.
# In append mode even if we move the cursor to the start of the file using seek() then  also it will write at
# the end of the file ONLY.


# In[5]:


# with open('f2.py' , 'a') as f:
#     f.tell()


# with open('Tax_proof.txt' , 'a') as f:
#     print(f.tell())
#     f.seek(0)
#     f.write('Hello')   
#     print(f.read())    #  UnsupportedOperation: not readable
    
# In the above case even we would get error bcoz of read() the content will be appended to the file .


# In[8]:


#  Append and read Mode -  a+
# If the file exists then  it will open the file in append mode and places the cursor at the end of the file.
# If the file does not exist then it will create the file 
# In this mode we are only allowed to write and read from the file.
# In append mode even if we move the cursor to the start of the file using seek() then  also it will write at
# the end of the file ONLY.

# with open('Tax_proof.txt' , 'a+') as f:
#     print(f.tell())
#     f.seek(0)
#     f.write('Hello')   
#     print(f.read())  # here we need to again use the seek() to read the file from begining 
#                      # as after write the cursor is at the end of file.

        
# with open('Tax_proof.txt' , 'a+') as f:
#     print(f.tell())
#     f.seek(0)
#     f.write('Hello') 
#     f.seek(0)
#     print(f.read())  # here we need to again use the seek() to read the file from begining 
                     # as after write the cursor is at the end of file.


# In[13]:


#  To read the file 

# read() - Reads the whole content of the file from the current cursor position and returns a string object .
# read(no_of_char) - Reads the specified no of chars from the current cursor position from the file and returns string object .
# readline() - Reads the  current line from the current cursor position and returns a string object.
# readlines() - Reads the whole content of the file from the current cursor position and returns a list of strings where each string is a line .


with open('Tax_proof.txt' , 'r+') as f:
#     content = f.read()
#     print(content , type(content))

#         f.seek(10)
#         content = f.read(10)
#         print(content , type(content))

#         content = f.readline()
#         print(content, type(content))

#         content =f.readlines()
#         print(content, type(content))


# In[17]:


# To write the content into the file 
# write('str')
# writelines(['str1\n' , 'str2\n' , 'str3\n' , 'str4\n' , 'str5\n' .... ])

# with open('Tax_proof_copy.txt' , 'w+') as f:
#     f.writelines(['Copy of the Certificate from Financial Institution for the interest payable on Housing \n', 'loan giving the break up of interest and principal repayment for the current financial \n', 'year 2022-23 and the date of loan sanction.\n', '\n', 'SSY passbook copy for the deposit made in the FY2022-23.\n', '\n', 'LIC premium receipt for FY2022-23.\n', '\n', 'Tuition fees paid during the FY2022-23, admission fees and  donations are not considered for Tax exemption.\n', '\n', 'Medical insurance premium paid  during the FY2022-23 under sec 80D for tax exemption.Hello'])
#     f.seek(0)
#     print(f.read())
    
#     f.write('''Copy of the Certificate from Financial Institution for the interest payable on Housing 
# loan giving the break up of interest and principal repayment for the current financial 
# year 2022-23 and the date of loan sanction.

# SSY passbook copy for the deposit made in the FY2022-23.

# LIC premium receipt for FY2022-23.

# Tuition fees paid during the FY2022-23, admission fees and  donations are not considered for Tax exemption.

# Medical insurance premium paid  during the FY2022-23 under sec 80D for tax exemption.Hello''')


# In[ ]:


# What is Lorem Ipsum?
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
# Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
# It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
# It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
# Why do we use it?
# It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.
# The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. 
# Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for lorem ipsum will uncover many web sites still in their infancy. 
# Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).


# In[14]:


# Count total no of words ,  total no of chars , total  no of lines .

# with open('my_file.txt', 'r') as fo:
#     content = fo.readlines()
#     print("Total no of characters in the file is : ",fo.tell())
#     print(content)
#     print("The no of lines in the file is : ", len(content))
#     fo.seek(0)
#     print("Total no nof words : ", len(fo.read().split() ))
    


# In[15]:


# Read the imgage file in visual format :

# from PIL import Image

# img = Image.open('Python.jpeg')
# img


# In[16]:


# Binary file handling 
# Copy the binary content  python.jpeg (image file)  and write it to new.png file 

# with open('python.jpeg', 'r+b') as fr:
#     content = fr.read()
#     with open('new.png', 'w+b') as  fw:
#         fw.write(content)

# with open('python.jpeg', 'r+b') as fr:
#     with open('new1.png', 'w+b') as  fw:
#         fw.write(fr.read())


# In[ ]:


# pickling and unpickling - pickle - learn abt this topic 


# # Exception Handling
# 
# 

# In[24]:


# Types of Error: 
#     1.  Compile Time Error -  syntax error , Indentation error
#     2. Run time Error -  ValueError , NameError , TypeError,  KeyError , IndexError
    
# Exceptions -  runtime error which can be handled are called Exceptions .

# Exception handling - try , except ,  else , finally , raise

# num1 = int(input('enter the first number :'))
# num2 = int(input('enter the second number :'))

# try:
#     print('Python'[9])
# #     res = num1/num2
# except:
#      print('2nd number is zero')
# else:
#     print(res)


# In[ ]:


# try - the code section which might raise error should be written within "try" block
# except -  this is alternate block of code which  needs to be executed in case any "Exception" is raised.
# else - this is the block of code which should be executed in case there are no errors.
# finally - irrespective of the error whatever code we want to  execute should be kept in finally  block.


# In[30]:


# try: 
#     num1 = int(input('enter the first number :'))
#     num2 = int(input('enter the second number :'))
#     res = num1/num2
#     print(num1 + 'Python')
# except ZeroDivisionError:
#     print('A number cannot be divided by 0')
# except ValueError:
#     print('int() function only accepts Integer value')
# except TypeError:
#     print('String type can only be concateneted with string')    

#  For one try block we can have multiple except block 
#  For every except block there must be one try block

# TO GET THE DEFAULT MESSAGE FOR EACH predefined / builtin exception we can do as below :

# try: 
#     num1 = int(input('enter the first number :'))
#     num2 = int(input('enter the second number :'))
#     res = num1/num2
#     print(num1 + 'Python')
# except ZeroDivisionError as e1:
#     print('A number cannot be divided by 0')
#     print(e1)
# except ValueError as e2:
#     print('int() function only accepts Integer value')
#     print(e2)
# except TypeError as e3:
#     print('String type can only be concateneted with string')  
#     print(e3)


# In[32]:


# try: 
#     num1 = int(input('enter the first number :'))
#     num2 = int(input('enter the second number :'))
#     res = num1/num2
#     print(num1 + 'Python')
# except (ZeroDivisionError , ValueError , TypeError) as e1:  #  One except block for all the exceptions 
#     print('common code')
#     print(e1)


# In[33]:


# Default Exception Block
# It should always be placed at the end .


# try: 
#     num1 = int(input('enter the first number :'))
#     num2 = int(input('enter the second number :'))
#     res = num1/num2
#     print('Python'[9])
# except ZeroDivisionError as e1:
#     print('A number cannot be divided by 0')
#     print(e1)
# except ValueError as e2:
#     print('int() function only accepts Integer value')
#     print(e2)
# except TypeError as e3:
#     print('String type can only be concateneted with string')  
#     print(e3)
# except Exception  as e:
#     print('Exception block')
#     print(e)


# In[35]:


# Nested try-except Block:

# try: 
#     num1 = int(input('enter the first number :'))
#     num2 = int(input('enter the second number :'))
#     res = num1/num2
#     try:
#         num3  = int(input('enter the third number :'))
#         print(num1/num3)
#     except:
#         print('3rd number cannot be 0')
# except:
#     print('2nd number cannot be 0')
        


# In[37]:


# try: 
#     num1 = int(input('enter the first number :'))
#     num2 = int(input('enter the second number :'))
#     res = num1/num2
# except:
#     print('2nd number cannot be 0')
# else:
#     print(res) # this code inside else block is ONLY excuted when there is no ERROR in try block.

# print(num1)
# print(num2)


# In[38]:


# f = open('f2.py' ,  'a')

# try:
#     f.write('\n\n\n This is  Python Class @Learnbay !!')
#     f.read() 
# except:
#     print('Read is not allowed in Append mode')
# finally:
#     print('Inside finally ....')
#     f.close()


# In[40]:


# User Defined Exceptions

# class myException(Exception):
#     def __init(self, msg):
#         self.m = msg


# In[41]:


# def deposit_amount(amt):
#     if amt > 50000:
#         raise myException('Amount is greater than 50k')
#     else:
#         print('Amount is deposited...')


# In[42]:


# deposit_amount(45000)


# In[44]:


# try:
#     deposit_amount(35000000)
# except myException as e :
#     print(e)


# In[25]:


# print(dir(__builtins__))


# In[ ]:


# Regular Expression : 

'''
[]  	 A set of characters	"[a-m]"	
\   	Signals a special sequence (can also be used to escape special characters)	"\d"	
.   	Any character (except newline character)	"he..o"	
^   	Starts with	"^hello"	
$   	Ends with	"planet$"	
*   	Zero or more occurrences	"he.*o"	
+   	One or more occurrences	"he.+o"	
?   	Zero or one occurrences	"he.?o"	
{}  	Exactly the specified number of occurrences	"he.{2}o"	
|   	Either or	"falls|stays"	
()  	Capture and group

\d  	 Digit [0-9]  
\D  	 Anything except (0-9)    
\w  	 Alphanumeric character(a-z . A-Z, 0-9 , _)
\b  	

 ".       - Any Character Except New Line\n",
    "\\d      - Digit (0-9)\n",
    "\\D      - Not a Digit (0-9)\n",
    "\\w      - Word Character (a-z, A-Z, 0-9, _)\n",
    "\\W      - Not a Word Character\n",
    "\\s      - Whitespace (space, tab, newline)\n",
    "\\S      - Not Whitespace (space, tab, newline)\n",
    "\n",
    "\\b      - Word Boundary\n",
    "\\B      - Not a Word Boundary\n",
    "^       - Beginning of a String\n",
    "$       - End of a String\n",
    "\n",
    "[]      - Matches Characters in brackets\n",
    "[^ ]    - Matches Characters NOT in brackets\n",
    "|       - Either Or\n",
    "( )     - Group\n",
    "\n",
    "Quantifiers:\n",
    "*       - 0 or More\n",
    "+       - 1 or More\n",
    "?       - 0 or One\n",
    "{3}     - Exact Number\n",
    "{3,4}   - Range of Numbers (Minimum, Maximum)\n",
    "\n",
    "\n",
    "#### Sample Regexs ####\n",
    "\n",
    "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+\n",
    "\n",
'''


# In[1]:


import re


# In[ ]:


# match - match method matches the pattern at the  begining of the string and returns a match object 
#         for this we use group .

# search - search method matches the pattern in the string for the first occurence of the pattern and returns a match object

# finadall - finds all the occurences of the pattern and returns a list object.
# finditer - finds all the occurences of the pattern and returns an iterator object of match object 

# NOTE - If we get the match  object to  extract the information  from macth object we use group method.


# In[2]:


# with open('f2.py' , 'r') as f:
#     content = f.read()
#     pattern = r'\wat'
#     res = re.match(pattern , content)   
#     print(res.group())
#     print(res.span())
#     print(res.span()[0], res.span()[1] )

# match method searches for the pattern at the begining of the file , if there is no pattern it will return None
# here in above case our file has "9a9t" in the starting which does not matches r\wat so returned None.


# In[3]:


# with open('f2.py' , 'r') as f:
#     content = f.read()
#     pattern = r'\wat'
#     res = re.search(pattern , content)
#     print(res.group())
#     print(res.span())
#     print(res.span()[0], res.span()[1] )


# In[4]:


# with open('f2.py' , 'r') as f:
#     content = f.read()
#     pattern = r'\wat'
#     res = re.findall(pattern , content)
#     print(res)


# In[7]:


with open('f2.py' , 'r') as f:
    content = f.read()
    pattern = r'\wat'
    for i in re.finditer(pattern , content):
        print(i.group())
        print(i.span())
        print(i.span()[0])
        print(i.span()[1])
        print()
        
# finditer method will return an iterator object of match object,  so we need to run the loop and group function to get the 
# results .


# In[9]:


text_to_search = '''
9a9t 99at c9T mat bat rat hat
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ\\s
321-555-4321
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \\ | ( )
guptaabhishek.com
abhishek-8765-gupta@yahoo.com
abhi_gyupta@gamil.abc
321-555-4321
123.555.1234
123*555*1234
123.555.1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr hello
abhsihek.gupta@gmail.com
abhishek-1234gupta@gmail.org
abhishek@hotmail.net
'''


# In[14]:


import re 
pattern = r'.'

res = re.finditer(pattern, text_to_search)
for i in  res:
    print(i)


# In[15]:


import re 
pattern = r'\s'

res = re.finditer(pattern, text_to_search)
for i in  res:
    print(i)


# In[16]:


# To match a non-space character

import re 
pattern = r'\S'

res = re.finditer(pattern, text_to_search)
for i in  res:
    print(i)


# In[17]:


# To match all the digits 
pattern = r'\d'

res = re.finditer(pattern, text_to_search)
for i in  res:
    print(i)


# In[18]:


import re 
pattern = r'\D'

res = re.finditer(pattern, text_to_search)
for i in  res:
    print(i)


# In[19]:


import re 
pattern = r'\w'

res = re.finditer(pattern, text_to_search)
for i in  res:
    print(i)


# In[20]:


import re 
pattern = r'\W'

res = re.finditer(pattern, text_to_search)
for i in  res:
    print(i)


# In[21]:


import re 
pattern = r'\.'

res = re.finditer(pattern, text_to_search)
for i in  res:
    print(i)


# In[23]:


import re 
string = 'cat catherine catholic wildcat cat copycat uncatchable'
pattern = r'cat'

res = re.finditer(pattern, string)
for i in  res:
    print(i)


# In[28]:


import re 
string = 'cat catherine catholic wildcat cat copycat uncatchable'
pattern = r'\bcat\b'

res = re.finditer(pattern, string)
for i in  res:
    print(i)


# In[32]:


import re 
string = 'cat catherine catholic wildcat cat copycat uncatchable'
pattern = r'^cat'

res = re.finditer(pattern, string)
for i in  res:
    print(i)


# In[33]:


import re 
string = 'cat catherine catholic wildcat cat copycat uncatchable'
pattern = r'able$'

res = re.finditer(pattern, string)
for i in  res:
    print(i)

