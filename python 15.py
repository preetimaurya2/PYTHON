#!/usr/bin/env python
# coding: utf-8

# In[ ]:


31.Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print all strings line by line. 


# In[1]:


def string():
    n1=input('enter string:')
    n2=input('enter string:')
    if len(n1)>len(n2):
        print(n1)
    elif len(n2)>len(n1):
        print(n2)
    else: 
        print(n1)
        print(n2)
    
string()    


# In[ ]:


32.Define a function that can accept an integer number as input and print the "It is an even number" if the number is 
even, otherwise print "It is an odd number". 


# In[ ]:


def even_odd():
    
    n=int(input('enter'))
    
    if (n%2==0):
        print('it is an even number:',n)
    else:
        print('it is an odd number:',n)
        
even_odd()        

