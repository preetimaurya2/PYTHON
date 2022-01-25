#!/usr/bin/env python
# coding: utf-8

# In[ ]:


18.A website requires the users to input username and password to register. Write a program to check the validity of 
password input by users. 
Following are the criteria for checking the password: 
1. At least 1 letter between [a-z] 
2. At least 1 number between [0-9] 
1. At least 1 letter between [A-Z] 
3. At least 1 character from [$#@] 
4. Minimum length of transaction password: 6 
5. Maximum length of transaction password: 12 


# In[3]:


def check_password():
    n=input('enter:').split(',') 
    
    for i in n:        
        a=0
        b=0
        c=0
        d=0
        for j in i:
            if j.islower():
                a=a+1
            elif j.isdigit():
                b=b+1
            elif j.isupper():
                c=c+1
            else:
                d=d+1
        if a>0 and b>0 and c>0 and d>0 and 6<=len(i)<=12:
           
            print('valid password:',i)
        else:
            print('invalid password:',i)
check_password()        
    


# In[ ]:


19. You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, 
age and height are numbers. The tuples are input by console. The sort criteria is: 
1: Sort based on name; 
2: Then sort based on age; 
3: Then sort by score. 

The priority is that name > age > score.
If the following tuples are given as input to the program: 
Tom,19,80 
John,20,90 
Jony,17,91 
Jony,17,93 
Json,21,85 


# In[20]:


from operator import itemgetter
det=()
tem=()
n=int(input('enter n'))
for i in range(n+1):
    name=input('enter name')
    age=input('enter age')
    score=input('enter score')
    tem=(name,age,score)
    det=det+(tem,)
print(det)
a=sorted(det,key=itemgetter(0,1,2))     #(0=name , 1=age ,2=score)
print(a,end=',')


# In[ ]:




