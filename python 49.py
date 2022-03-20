#!/usr/bin/env python
# coding: utf-8

# In[ ]:


89. Please write a program which count and print the numbers of each character in a string input by console. 
If the following string is given as input to the program: abcdefgabc 


# In[ ]:


n=input('please enter string')
a=[]
for i in n:
    if i not in a:
        a.append(i)
        print(i,',',n.count(i))


# In[ ]:


90. Please write a program which accepts a string from console and print it in reverse order. 
If the following string is given as input to the program: rise to vote sir 
Then, the output of the program should be: ris etov ot esir 


# In[ ]:


n=input('enter')
n=n[::-1]
print(n)

