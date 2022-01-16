#!/usr/bin/env python
# coding: utf-8

# In[ ]:


3. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral
number between 1 and n (both included) and then the program should print the dictionary. 
Suppose the input is supplied to the program: 8 
Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} 


# In[1]:


c={i:i*i for i in range(1,9)}
print(c)


# In[ ]:


4.Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number. 
Suppose the input is supplied to the program: 34, 67, 55, 33, 12, 98 
Then, the output should be: 
['34', '67', '55', '33', '12', '98'] 
('34', '67', '55', '33', '12', '98') 


# In[2]:


a=input('enter').split(',')
b=[]
for i in a:
    b.append(i) 
    
print(b)

c=tuple(b)
print(c)    


# In[ ]:




