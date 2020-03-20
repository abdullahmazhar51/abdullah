#!/usr/bin/env python
# coding: utf-8

# In[10]:


f = open("abdullah.txt", "r")


# In[11]:


output = f.readlines()


# In[12]:


print(output)


# In[25]:


i = 0
for line in output:
    print(i, line.strip())
    i += 1


# In[23]:


#csv write


# In[46]:


f_out = open("mangal.txt", "w")


# In[47]:


f_out.writelines(output[1])


# In[48]:


f_out.close()


# In[56]:


fav_lines = [0, 1]


# In[57]:


with open("mangal.txt", "w") as f_out:
    for fav_line in fav_lines:
        f_out.writelines(output[fav_line])


# In[58]:


fav_lines2 = [2]


# In[59]:


with open("mangal.txt", "w") as f_out:
    for fav_line2 in fav_lines2:
        f_out.writelines(output[fav_line2])


# In[ ]:




