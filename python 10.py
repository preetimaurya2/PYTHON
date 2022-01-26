#!/usr/bin/env python
# coding: utf-8

# In[ ]:


20.Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n. 


# In[1]:


class number:
    def __init__(self):
        n=int(input('enter number'))
        self.n=n
    def show(self):
        for i in range(0,(self.n)+1):
            if (i%7==0):
                yield(i)
num=number()
print(num.show())
for i in num.show():
    print(i,end=',')
    


# In[ ]:


21.A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT 
with a given steps. The trace of robot movement is shown as the following: 
UP 5 
DOWN 3 
LEFT 3 
RIGHT 2 

The numbers after the direction are steps. Please write a program to compute the distance from current position after a 
sequence of movement and original point. If the distance is a float, then just print the nearest integer. 


# In[2]:


import math

UP=int(input('enter up'))
DOWN=int(input('enter down'))
LEFT=int(input('enter left'))
RIGHT=int(input('enter right'))

B=(UP-DOWN)
C=(LEFT-RIGHT)

D=math.sqrt(B**2+C**2)

print(round(D))


# In[ ]:




