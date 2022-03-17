#!/usr/bin/env python
# coding: utf-8

# In[ ]:


83. By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0. 
Hints: Use list comprehension to make an array. 


# In[3]:


a=[[[0*(i*j*k) for j in range(3)]for i in range(5)]for k in range(8)]
print(a)


# In[ ]:


84. By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in 
[12,24,35,70,88,120,155]. 
Hints: Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple. 


# In[5]:


a=[12,24,35,70,88,120,155]
b=[0,4,5]
c=[x for (i,x) in enumerate(a) if i not in b]
print(c)

