#!/usr/bin/env python
# coding: utf-8

# In[ ]:


61. Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0). 
If the following n is given as input to the program: 5 
Then, the output of the program should be: 3.5


# In[ ]:


n=int(input('enter the number'))
s=0
for i in range(1,n+1): 
    
    s=s+(i/(i+1))
    
print(round(s,1))    


# In[ ]:


62. Write a program to compute: 

f(n)=f(n-1)+100 when n>0 
and f(0)=1 
with a given n input by console (n>0). 
If the following n is given as input to the program: 5 
Then, the output of the program should be: 500 


# In[2]:


def f(n): 
    if n==0:
        return 1
    if n==1:
        return 100
    if n>1:
        return (f(n-1)+100)
    
    f(n)
f(5)       

