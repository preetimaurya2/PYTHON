#!/usr/bin/env python
# coding: utf-8

# In[ ]:


87.  With a given list [12, 24, 35, 24, 88, 120, 155, 88, 120, 155], write a program to print this list after removing all 
duplicate values with original order reserved. 
Hints: Use set() to store a number of values without duplicate.


# In[1]:


a=[12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)        


# In[ ]:


88. Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can 
print "Male" for Male class and "Female" for Female class. 
Hints: Use Subclass(Parentclass) to define a child class. 


# In[4]:


class Person:    
    def getGender(self):
        print('unknown')  
        
class Male(Person):
    def __init__(self,male):
        self.male=male
        
    def getGender(self):
        return f'{self.male} is male'
    
class Female(Person):
    def __init__(self,female):       
        self.female=female
        
    def getGender(self):
            return f'{self.female} is female'
        
obj1=Male('ram') 
obj2=Female('sita')
print(obj1.getGender())
print(obj2.getGender())

