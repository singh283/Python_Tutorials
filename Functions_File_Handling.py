#!/usr/bin/env python
# coding: utf-8

# In[7]:


# in_str = 'This is Python Class'
# lst = []

# lst = list(in_str.split())

# print(lst, type(lst) , len(lst))

# out_str = str(' '.join(lst[::-1]))

# print(out_str)


# In[42]:


# in_str = 'This is Python Class'
# lst = []
# out_str = '' 

# for i  in range(len(in_str)):
#     if in_str[i] == ' ' :
#         out_str = ' ' + out_str
#     else:
#         out_str = in_str[i] + out_str
        
# print(out_str)


# In[12]:


# in_str = 'This is Python Class'
# out_str = '' 
# out_lst = [] 


# for i  in range(-1, -len(in_str)-1, -1):
#     if in_str[i] == ' ' :
#         out_lst.append(out_str)
#         out_str= ''
#     else:
#         out_str = out_str + in_str[i] 

# out_lst.append(out_str)
# print(out_lst)

# out_lst = str(' '.join(out_lst[::-1]))
        
# print(out_lst)


# In[7]:


# in_str = 'This is Python Class'
# out_str = '' 
# out_lst = [] 


# for i  in range(len(in_str)):
#     if in_str[i] == ' ' :
#         out_lst.append(out_str)
#         out_str= ''
#     else:
#         out_str = out_str + in_str[i] 

# out_lst.append(out_str)
# print(out_lst)

# out_lst = str(' '.join(out_lst[::-1]))
        
# print(out_lst)


# In[14]:


# in_str = 'This is Python Class'
# out_str = '' 
# out_lst = [] 


# for i  in range(len(in_str)):
#     if in_str[i] == ' ' :
#         out_lst.append(out_str)
#         out_str= ''
#     else:
#         out_str = in_str[i] + out_str

# out_lst.append(out_str)
# print(out_lst)

# out_lst = str(' '.join(out_lst[::-1]))
        
# print(out_lst)


# In[1]:


# import sqrt
# print(__name__)

# when we are importing any python script (module) in current module and if the import module has any  executable code whicc is 
#  not written within __main__ namespace then it gets executed because after importing that  module is running under current namespace
# and here in this current module that value of __name__ is '__main__'

# However if we want that  while imporitng the required module into current module it should not execute the executable code 
# while importing we need to put the executable statements and function calling  inside __name__ = '__main__' block


# In[6]:


# import sqrt_dup

# print(__name__)

# here we have put all the executable statements and function calling  inside __name__ = '__main__' block so while importing this 
# module here it is not excuting the statements and excutables 

# Because inside that module("sqrt_dup") the value of __name__ is the file name and not __main__ so enclosing statements 
# are  not executed .

# however  if we copy+paste the complete code from that module OR remove the condition 
# if __name__ == '__main__'  
# then it will start executing because the code will be excuting under current module and here the value of __name__ is '_main_'


# In[4]:


# from math import sqrt


# def find_sqrt(num):
# 	res =  sqrt(num)
# 	print(f'sqrt of {num}  is : ' , res)

# print('__name__ is :', __name__)


# if __name__ == '__main__':
#     num = eval(input('Enter the number: '))
#     find_sqrt(num)


# In[ ]:


# file handling in Python 

# Types of file 
#     1.Text file 
#     2.Binary file 
    
# f = open('file_name.ext',  mode )
# f.read()
# f.write()
# f.close()

# In above case file needs to be closed at the end of the program else it will throw the error.


# with open('file_name.ext',  mode ) as f: 
#     f.read()
#     f.write()
    
    
# In case of with even if the file is not closed at the end of program , it will be handled automatically.


# In[ ]:


#  Modes of opereation in text files :

# read  - r
# write - w
# read and write -  r+
# write and read - w+
# append - a+
# append and read - a+

#  Modes of operation in Binary files:

# read  - rb
# write - wb
# read and write -  r+b
# write and read - w+b
# append - a+b
# append and read - a+b


# In[19]:


# File object considers the content of the file as a string .

#  read  - r

# If the file exist then it will open the file in read mode and places the cursor at the begining of the file .
# If the file does not exist it will throw 'filenotfound' error.
# In this mode you are only  allowed to read the file .

# with open('file.py' , 'r') as f:    FileNotFoundError: [Errno 2] No such file or directory: 'file.py'
#     f.read()

# with open('Tax_proof.txt' , 'r') as f:
#     print('Cursor position just after opening the file : ', f.tell())
#     print(f.read())
#     print('Cursor position after reading the whole file : ', f.tell())  

    
# So there are 218 characters in this file 


# In[23]:


#  read an write  - r+

# If the file exist then it will open the file in read mode and places the cursor at the begining of the file .
# If the file does not exist it will throw 'filenotfound' error.
# In this mode you are only  allowed to read and write the file .



# with open('Tax_proof.txt' , 'r+') as f:
#     print('Cursor position just after opening the file : ', f.tell())
#     print(f.read())
#     print('Cursor position after reading the whole file : ', f.tell())  
#     f.write('\n ***** End ******* ')
#     f.seek(0)   # This will place the curor at the begining of the file and if we write any content after it file content 
#                 # will be overwritten with whatever content we want to write in the file.
#     f.write('Tax Proof Submission Guidelines \n') 
#     print(f.read())


# In[5]:


# with open('Tax_proof.txt' , 'r+') as f:
#     print('Cursor position just after opening the file : ', f.tell())
#     print('Cursor position after reading the whole file : ', f.tell())  
#     f.read()
#     f.write('\n ***** End ******* ')
#     f.seek(0)
#     f.write('Tax Proof Submission Guidelines\n' + content) 
# #     print(f.read())


# In[7]:


#  write  - w

# If the file exist then it will open the file in write mode and DELETES the content of the file and overw
# If the file does not exist it will give a new name to the file 
# In this mode you are only  allowed to write and not read the file .


# with open('Tax_proof.txt' , 'w') as f:
#     print('Cursor position just after opening the file : ', f.tell())
#     print('Cursor position after reading the whole file : ', f.tell())  
#     f.read()   # UnsupportedOperation: not readable and THE CONTENT OF THE FILE IS DELETED , will now have empty file 
#     f.write('\n ***** End ******* ')
    
    
    
# with open('Tax_proof.txt' , 'w') as f:
#     print('Cursor position just after opening the file : ', f.tell())
#     print('Cursor position after reading the whole file : ', f.tell())  
#     f.write('\n ***** End ******* ')



#  write and read mode  - w+

# If the file exist then it will open the file in write mode and DELETES the content of the file and overw
# If the file does not exist it will give a new name to the file 
# In this mode you are only  allowed to write and read the file .

