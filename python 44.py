#!/usr/bin/env python
# coding: utf-8

# In[ ]:


77. Please write a program to randomly print a integer number between 7 and 15 inclusive. 
Hints: Use random.randrange() to a random integer in a given range. 


# In[4]:


import random
print(random.randrange(7,15))


# In[ ]:


78. Please write a program to shuffle and print the list [3,6,7,8]. 
Hints: Use shuffle() function to shuffle a list. 


# In[3]:


from random import shuffle
a=[3,6,7,8]
shuffle(a)
a

