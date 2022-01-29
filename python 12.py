#!/usr/bin/env python
# coding: utf-8

# In[ ]:


24. Python has many built-in functions, and if you do not know how to use it, you can read document online or find some 
books. But Python has a built-in document function for every built-in functions. Please write a program to print some 
Python built-in functions documents, such as abs(), int(), raw_input() And add document for your own function 
Hints: The built-in document method is __doc__ 


# In[ ]:


def cube(num):
    'Return the cube value of the input number'
    
    return num ** 3

print cube(2)

print abs.__doc__
print int.__doc__
print raw_input.__doc__


# In[ ]:


25. Define a class, which have a class parameter and have a same instance parameter. 


# In[2]:


class bird:
    name='Blue'
    def __init__(self,name):
        self.name=name
        
    def sing(self,song):
        return f'{self.name} is singing {song}.'
    
bir=bird('"Green"')
print(bir.sing('"Hello"'))

