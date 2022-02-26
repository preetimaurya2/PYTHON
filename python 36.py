#!/usr/bin/env python
# coding: utf-8

# In[ ]:


66. Please write a program using  generator to print the numbers which can be divisible by 5 and 7 between 0 and n in
comma separated form while n is input by console. 
If the following n is given as input to the program: 100 
Then, the output of the program should be: 0, 35, 70 


# In[ ]:


def divisible(n):
    
    for i in range(0,n):
        if (i%5==0) and (i%7==0):
            yield (i)
            
divisible(100)

for i in (divisible(100)):
    print(i,end=',')

