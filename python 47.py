#!/usr/bin/env python
# coding: utf-8

# In[ ]:


85. By using list comprehension, please write a program to print the list after removing the value 24 in
[12,24,35,24,88,120,155]. 
Hints: Use list's remove method to delete a value. 


# In[ ]:


a=[12,24,35,24,88,120,155]
a.remove(24)
print(a)


# In[ ]:


86. With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are 
intersection of the above given lists. 
Hints: Use set() and "&=" to do set intersection operation. 


# In[4]:


a=[1,3,6,78,35,55]
b=[12,24,35,24,88,120,155]
c=set(a).intersection(b)
print(c)

