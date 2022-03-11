#!/usr/bin/env python
# coding: utf-8

# In[ ]:


74. Please write a binary search function which searches an item in a sorted list. The function should return the index of
element to be searched in the list. 
Hints: Use if/elif to deal with conditions.


# In[ ]:


def search(n):
    
    n=sorted(n)
    i=int(input('enter'))
    
    if i in n:
        print(n.index(i),': index value')
    else:
        print('not in list')
        
    print('sorted list',n)
    
search([1,2,9,8,4,5,6])  

