#!/usr/bin/env python
# coding: utf-8

# In[ ]:


14. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
Suppose the input is supplied to the program: Hello world! 
Then, the output should be: UPPER CASE 1 
LOWER CASE 9 


# In[4]:


n=input('enter')
u=0
l=0
for i in n:
    if i.isupper():
        u=u+1

    elif i.islower():
        l=l+1
    else:
        pass
        
print('uppercase letters:',u)
print('lowercase letters:',l)
        


# In[ ]:


15.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. 


# In[1]:


n=int(input('enter value'))
a=9
s=0
for i in range(0,n):
    print(a,end='+')
    s=s+a
    a=a*10+9
print('sum of above series:',s)    


# In[ ]:




