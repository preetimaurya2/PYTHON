#!/usr/bin/env python
# coding: utf-8

# In[ ]:


51. Define a class named American and its subclass NewYorker. 
Hints: Use class Subclass(ParentClass) to define a subclass. 


# In[3]:


class American:
    pass
class New_Yorker(American):
    pass

america=American()
new_york=New_Yorker()

print(america)
print(new_york)


# In[ ]:


52. Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the 
area. 


# In[4]:


class circle:
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return f'area of circle :{3.14*(self.radius)**2}'
        
obj=circle(7)
print(obj.area())

