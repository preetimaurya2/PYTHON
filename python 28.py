#!/usr/bin/env python
# coding: utf-8

# In[ ]:


56. Define a custom exception class which takes a string message as attribute. 
Hints: To define a custom exception, we need to define a class inherited from Exception. 


# In[4]:


class exp(BaseException):
    def __init__(self,message):
        self.message=message
    
error=exp('string')
print(error)

