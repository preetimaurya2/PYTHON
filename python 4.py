#!/usr/bin/env python
# coding: utf-8

# In[ ]:


8.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated 
sequence after sorting them alphabetically. 


# In[9]:


n=input('enter words:').split(',')
print(sorted(n))


# In[ ]:


9.Write a program that accepts sequence of lines as input and prints the lines after making all 
characters in the sentence capitalized


# In[16]:


n=input('please enter the lines: ').split(',')
for i in n:
    a=i.upper()
    print(a)

