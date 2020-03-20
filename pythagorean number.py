#!/usr/bin/env python
# coding: utf-8

# In[1]:


#nested loop example


# In[2]:


from math import sqrt


# In[6]:


n = int(input("maximum number?\n"))
for a in range( 1, n+1):
    for b in range(a, n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2))==0:
            print(a, b, c)


# In[ ]:




