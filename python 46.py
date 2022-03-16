#!/usr/bin/env python
# coding: utf-8

# In[ ]:


81. By using list comprehension, please write a program to print the list after removing delete numbers which are divisible
by 5 and 7 in [12,24,35,70,88,120,155]. 
Hints: Use list comprehension to delete a bunch of element from a list. 


# In[ ]:


a=[12,24,35,70,88,120,155]
c=[i for i in a if (i%5!=0) and (i%7!=0)]
print(c)


# In[ ]:


82. By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in 
[12,24,35,70,88,120,155]. 
Hints: Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.


# In[5]:


a=[12,24,35,70,88,120,155]
b=[0,2,4,6]
c=[x for (i,x) in enumerate(a) if i not in b]
print(c)

