#!/usr/bin/env python
# coding: utf-8

# In[ ]:


59. Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of 
digits only. If the following words are given as input to the program: 2 cats and 3 dogs. 
Then, the output of the program should be: ['2', '3'] 


# In[1]:


n=input('please enter:')
a=[]
for i in n:
    if i.isdigit():
        a.append(str(i))
print(a)


# In[ ]:


60. Print a unicode string "hello world". 
Hints: Use u'strings' format to define unicode string. 


# In[1]:


a = u" hello world"
print(a)

