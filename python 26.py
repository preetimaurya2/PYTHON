#!/usr/bin/env python
# coding: utf-8

# In[ ]:


53.Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which 
can compute the area. 


# In[ ]:


class rectangle:
    
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
        
    def area(self):        
        return f'area of rectangle:{(self.lenght)*(self.width)}'
    
obj=rectangle(10,20)
print(obj.area())


# In[ ]:


54. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as 
argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default. 


# In[5]:


class Shape:
    def __init__(self):
        pass
        
    def area(self,length):
        return f'area of Square is:{(length)**2}'
        
class Square(Shape):    
    def area(self,length=0):
        return f'area:{(length)**2}'
        
obj=Square()

print(obj.area(10))

print(obj.area())

