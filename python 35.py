#!/usr/bin/env python
# coding: utf-8

# In[ ]:


65.Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is 
input by console. 
Example: If the following n is given as input to the program: 10 
Then, the output of the program should be: 0,2,4,6,8,10 


# In[ ]:


def even(n):
    for i in range(0,n):
        if i%2==0:
            yield(i)
even(10)
for i in even(10):
    print(i,end=',')
