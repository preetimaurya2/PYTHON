#!/usr/bin/env python
# coding: utf-8

# In[ ]:


37. Define a function which can generate and print a list where the values are square of numbers between 1 and 20 
(both included). 


# In[ ]:


def square():
    
    a=[]
    
    for i in range(1,21):
        a.append(i**2)
        
    print(a)
    
square()


# In[ ]:


38. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list. 


# In[ ]:


def square():
    a=[]
    for i in range(1,21):
        a.append(i**2)
    print(a[:5])
square()
        

