#!/usr/bin/env python
# coding: utf-8

# In[ ]:


12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the 
number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.


# In[ ]:


for i in range(1000,3001):
    i=str(i)
    c=0
    for j in i:
        j=int(j)
        if(j%2==0):
            c=c+1
    if c==4:
        print(i,end=',')       


# In[ ]:


13. Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the input is supplied to the program: hello world! 123 
Then, the output should be: LETTERS 10
DIGITS 3 


# In[ ]:


n=input('enter letters and digits')
c=0
d=0
for i in n:
    if i.isalpha():
        c=c+1
    elif i.isdigit():
        d=d+1
    else:
        pass
print('Letters:',c)
print('Digits:',d)

