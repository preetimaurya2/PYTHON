#!/usr/bin/env python
# coding: utf-8

# In[ ]:


79. Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and 
the object is in ["Hockey","Football"]. 
Hints: Use list[index] notation to get a element from a list. 


# In[ ]:


s=["I", "You"]
v=["Play", "Love"]
o=["Hockey","Football"]
for i,j,k in zip(s,v,o):
    print(i+' '+j+' '+ k)


# In[ ]:


80. Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24]. 
Hints: Use list comprehension to delete a bunch of element from a list. 


# In[ ]:


a=[5,6,77,45,22,12,24]
c=[i for i in a if (i%2!=0) ]
print(c)

