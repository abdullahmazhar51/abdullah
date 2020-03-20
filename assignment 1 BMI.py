#!/usr/bin/env python
# coding: utf-8

# In[37]:


#assignment problems 1


# In[42]:


record_weight = float(input(" my weight in kg "))


# In[43]:


height_f = float(input(" my height in foot "))


# In[44]:


height_I = float(input(" my height in inches "))


# In[45]:


height_M = height_f / 3.281


# In[46]:


print(height_M)


# In[47]:


BMI = record_weight / height_M**2


# In[53]:


print(BMI)


# In[57]:


if BMI < 18.5:
    print("UNDERWEIGHT")
elif BMI >= 18.5 and BMI < 25:
    print("NORMAL")
elif BMI >= 25 and BMI <30:
    print("OVERWEIGHT")
elif BMI >= 30:
    print("VERY-OVERWEIGHT")


# In[ ]:




