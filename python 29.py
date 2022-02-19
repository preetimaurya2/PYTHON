#!/usr/bin/env python
# coding: utf-8

# In[ ]:


57. Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the
user name of a given email address. Both user names and company names are composed of letters only. 
If the following email address is given as input to the program: Chandra@gdhdhtc.com 
Then, the output of the program should be: Chandra 

In case of input data being supplied to the question, it should be assumed to be a console input. 


# In[5]:


n=input("please enter the email address")
for i in n:
    if i=='@':
        break
    print(i,end='')    

