#!/usr/bin/env python
# coding: utf-8

# In[ ]:


47. Write a program which can map() and filter() to make a list whose elements are square of even number in 
[1,2,3,4,5,6,7,8,9,10]. 


# In[1]:


def even_square():
    
    b=list(filter(lambda i:(i%2==0),[1,2,3,4,5,6,7,8,9,10]))    
    a=list(map(lambda i:i**2,b))
    
    print(a)
    
even_square()    


# In[ ]:


48. Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included). 


# In[11]:


list(filter(lambda i:(i%2==0),range(21)))

