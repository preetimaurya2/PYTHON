#!/usr/bin/env python
# coding: utf-8

# In[ ]:


49. Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included). 


# In[ ]:


def square():  
    
    a=list(map(lambda i:i**2,range(1,21)))
    print(a)
    
square()   


# In[ ]:


50. Define a class named American which has a static method called printNationality. 


# In[2]:


class American:
    @staticmethod
    def printNationality():
        print(' american nationality')

america=American()
america.printNationality()
American.printNationality()

