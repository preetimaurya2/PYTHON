#!/usr/bin/env python
# coding: utf-8

# In[ ]:


35.Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the 
values are square of key.The function should just print the values only. 


# In[ ]:


def values():
    
    c={i:i**2 for i in range(1,21)}
    
    print(c.values())
    
values()   


# In[ ]:


36. Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the 
values are square of keys. The function should just print the keys only. 


# In[ ]:


def keys():
    
    c={i:i**2 for i in range(1,21)}
    
    print(c.keys())
    
keys()  

