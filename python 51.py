#!/usr/bin/env python
# coding: utf-8

# In[ ]:


93.  Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? 
Hint: Use for loop to iterate all possible solutions 


# In[ ]:


heads=int(input('enter'))
legs=int(input('enter'))
y=((legs-2*heads)/2)
print('number of rabbits:',y)
z=(heads-y)
print('number of chickens:',z)


# In[ ]:


94.  Create a dictionary with phone numbers (phonebook = {“John”: 938477566, "Jack”: 938377264, "Jill”: 947662781}). 
Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.


# In[ ]:


phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
phonebook["Jake"]={938273443}
del phonebook['Jill']
print(phonebook)

