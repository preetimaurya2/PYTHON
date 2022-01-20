#!/usr/bin/env python
# coding: utf-8

# In[ ]:


10. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing 
all duplicate words and sorting them alphanumerically. 
Suppose the input is supplied to the program: hello world and practice makes perfect and hello world again 
Then, the output should be: again and hello makes perfect practice world 


# In[1]:


a=input('enter words:').split(' ')
l=[]
for i in a:
    if i not in l:
        l.append(i)
        
a=(sorted(l))

print(' '.join(a))


# In[ ]:


11. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether 
they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. 
Suppose the input is supplied to the program: 0100,0011,1010,1001 
Then the output should be: 1010 


# In[2]:


n=input('enter').split(',')
for i in n:
    if i[0]=='1':
        i=(int(i))
        if (i%5==0):
            print(i)


# In[ ]:




