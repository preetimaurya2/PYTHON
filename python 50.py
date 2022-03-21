#!/usr/bin/env python
# coding: utf-8

# In[ ]:


91.  Please write a program which accepts a string from console and print the characters that have even indexes. 

If the following string is given as input to the program: H1e2l3l4o5w6o7r8l9d 
Then, the output of the program should be: Helloworld 


# In[ ]:


n=input('enter string:')
n=n[::2]
print(n)


# In[ ]:


92. Please write a program which prints all permutations of [1, 2, 3] 
Hints: Use itertools.permutations() to get permutations of list. 


# In[ ]:


from itertools import permutations
a=[1,2,3]
print(list(permutations(a)))

