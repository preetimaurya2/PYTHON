#!/usr/bin/env python
# coding: utf-8

# In[ ]:


45. Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10]. 


# In[1]:


list(filter(lambda i:(i%2==0),[1,2,3,4,5,6,7,8,9,10]))


# In[ ]:


46. Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]. 


# In[2]:


list(map(lambda i:i**2,[1,2,3,4,5,6,7,8,9,10]))

