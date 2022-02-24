#!/usr/bin/env python
# coding: utf-8

# In[ ]:


64. The Fibonacci sequence is computed based on the following formula: 
f(n)=0 if n=0 
f(n)=1 if n=1 
f(n)=f(n-1)+f(n-2) if n>1 

Please write a program using list comprehension to print the Fibonacci sequence in comma separated form with a given 
n input by console. 
If the following n is given as input to the program: 7 
Then, the output of the program should be: 0, 1, 1, 2, 3, 5, 8, 13 


# In[ ]:


def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return (f(n-1)+f(n-2))
n=int(input('enter num:'))
c=[f(i) for i in range(0,n+1)]
print(c)

