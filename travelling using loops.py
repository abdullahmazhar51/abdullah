#!/usr/bin/env python
# coding: utf-8

# In[ ]:


travelling = input("Yes or No")
while travelling == 'yes':
    num = int(input("num of people travelling:"))
    
    for num in range(1, num + 1):
        name = input("name:")
        age = input("age:")
        sex = input("Male or Female:")
        print(name)
        print(age)
        print(sex)
    travelling = input("oops! forgot someone")


# In[ ]:




