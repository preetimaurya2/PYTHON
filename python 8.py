#!/usr/bin/env python
# coding: utf-8

# In[ ]:


16. Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated 
numbers. 


# In[ ]:


a=[1,2,3,4,5,6]
c=[i**2 for i in a if (i%2!=0)]
print(c)


# In[ ]:


17.Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following: 
D 100 
W 200 
--D means deposit while W means withdrawal. 


# In[2]:


i=1
balance=0
n=int(input('how many times deposits:'))
while i<(n+1):
    d=int(input('enter deposit amount:'))
    balance=balance+d
    i=i+1
else:
    print('deposit balance:',balance)
    
n=int(input('how many times withdrawal:'))    
i=1
while i<(n+1):
    W=int(input('enter withdrawn amount:'))
    balance=balance-W
    i=i+1
else:
    pass
    
print('total balance:',balance)  


# In[ ]:




