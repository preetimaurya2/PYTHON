#!/usr/bin/env python
# coding: utf-8

# In[ ]:


5.Define a class which has at least two methods: 
getString: to get a string from console input 
printString: to print the string in upper case. 
Also please include simple test function to test the class methods. 
Hints: Use __init__ method to construct some parameters 


# In[1]:


class string:
    def __init__(self):
        pass
    def getstring(self):
        self.n=input('enter:')
    def printstring(self):
        return (self.n.upper())
        
stri=string()
stri.getstring()
print(stri.printstring())


# In[ ]:


6.Write a program that calculates and prints the value according to the given formula: 
Q = Square root of [(2 * C * D)/H] 
Following are the fixed values of C and H: C is 50. H is 30.
    
D is the variable whose values should be input to your program in a comma-separated sequence. 


# In[4]:


def cal(D):
    C=50
    H=30
    Q = ((2 * C * D)/H)**(1/2) 
    return (round(Q))
cal(100)

list(map(cal,[100,150,180]))


# In[ ]:


7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j. 
Note: i=0,1.., X-1; j=0,1,¡Y-1. 
Suppose the following inputs are given to the program: 3, 5 
Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 


# In[3]:


import numpy as np
a=np.fromfunction(lambda i,j:i*j,(3,5))
print(a)

