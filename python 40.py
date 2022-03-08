#!/usr/bin/env python
# coding: utf-8

# In[ ]:


70. Please generate a random float where the value is between 5 and 95 using Python math module. 
Hints: Use random.random() to generate a random float in [0,1]. 


# In[2]:


import random
a=[i for i in range(5,95)]
print(random.random())


# In[ ]:


71. Please write a program to output a random even number between 0 and 10 inclusive using random module and list 
comprehension. 
Hints: Use random.choice() to a random element from a list. 


# In[1]:


import random
a=[i for i in range(1,11) if (i%2==0)]  
print(random.choice(a))

