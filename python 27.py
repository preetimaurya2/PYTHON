#!/usr/bin/env python
# coding: utf-8

# In[ ]:


55. Write a function to compute 5/0 and use try/except to catch the exceptions. 
Hints: Use try/except to catch exceptions. 


# In[ ]:


def fun():
    try:
        5/0
    except Exception as e:
        print('This block having some kind of exception')
fun()     

