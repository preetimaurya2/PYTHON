#!/usr/bin/env python
# coding: utf-8

# In[ ]:


22. Write a program to compute the frequency of the words from the input. The output should output after sorting the key 
alphanumerically.


# In[3]:


n=input('enter:').split(' ')
n=sorted(n)
a=[]
for i in n:
    if i not in a:
        a.append(i)
        x=n.count(i)
        print(i,':',x)


# In[ ]:


23.Write a method which can calculate square value of number .
Hints: Using the ** operator 


# In[1]:


def square():
    n=int(input('enter:'))          
    print(n**2)
square()

