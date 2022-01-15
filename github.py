#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.


# In[1]:


def div():
    for i in range(2000,3201):
        if (i%7==0) and (i%5!=0):
            print(i,end=' ,')
div()  


# In[ ]:


2.Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the input is supplied to the program: 8 
Then, the output should be: 40320 


# In[2]:


def factorial(*a):
    for n in a:
        if n==0:
            return 1
        elif n==1:
            return 1
        elif n>1:
            return (n*factorial(n-1))
factorial(8)
                    
list(map(factorial,[3,4,5,6,7,8]))


# In[ ]:




