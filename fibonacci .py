#!/usr/bin/env python
# coding: utf-8

# In[4]:


def fibonacci(n):
    if n<0:
        print("fibonacci doesnt exist")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci (n-1) + fibonacci(n-2)


# In[6]:


print(fibonacci(9))


# In[ ]:




