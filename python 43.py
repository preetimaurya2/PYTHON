#!/usr/bin/env python
# coding: utf-8

# In[ ]:


75. Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive. 
Hints: Use random.sample() to generate a list of random values.


# In[2]:


import random
c=[i for i in range(100,201) if (i%2==0)]
print(random.sample(c,5))


# In[ ]:


76. Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 
inclusive. 
Hints: Use random.sample() to generate a list of random values.


# In[1]:


import random
c=[i for i in range(1,1001) if (i%5==0) and (i%7==0)]
print(random.sample(c,5))

