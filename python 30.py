#!/usr/bin/env python
# coding: utf-8

# In[ ]:


58. Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the
company name of a given email address. Both user names and company names are composed of letters only. 
If the following email address is given as input to the program: Chandra@analytixlabs.com 
Then, the output of the program should be: analytixlabs 


# In[1]:


n=input("please enter the email address")
for i in n:
    x=n.index('@')
    y=n.rfind('.')
    a=n[x+1:y]
print(a)   

