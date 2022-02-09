#!/usr/bin/env python
# coding: utf-8

# In[ ]:


43. Write a program to generate and print another tuple whose values are even numbers in the given 
tuple (1,2,3,4,5,6,7,8,9,10). 


# In[2]:


t=()
a=(1,2,3,4,5,6,7,8,9,10)
for i in a:
    if (i%2==0):
        t=t+(i,)
print(t)        


# In[ ]:


44. Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes",
otherwise print "No".


# In[1]:


n=input('enter string:')

if n=='yes' or n=='YES' or n=='Yes':
    print('Yes')
else:
    print('No')

