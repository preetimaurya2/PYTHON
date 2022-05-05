#!/usr/bin/env python
# coding: utf-8

# In[ ]:


30.  Consider a generator function that generates 10 integers and use it to build an array 


# In[8]:


import numpy as np

def integer():
    for i in range(11):
        yield i
        
np.fromiter(interger(),dtype=float)        

