#!/usr/bin/env python
# coding: utf-8

# In[ ]:


41. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 
(both included). 


# In[12]:


def tuples():
    t=()
    for i in range(1,21):
        t=t+(i**2,)
    print(t) 
tuples()


# In[ ]:


42. With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half
values in one line. 


# In[11]:


def abc():
    a=(1,2,3,4,5,6,7,8,9,10)
    
    b=(len(a)//2)
    
    print(a[:b])
    print(a[b:])
    
abc()    

