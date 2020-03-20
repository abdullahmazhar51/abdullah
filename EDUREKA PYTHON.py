#!/usr/bin/env python
# coding: utf-8

# In[4]:


#declaration
x = 10
y = 2
print(x + y)


# In[5]:


#data types


# In[6]:


x = 10
print(type(x))


# In[8]:


x = 2.5
print(type(x))


# In[9]:


y = 10j
print(type(y))


# In[10]:


num = 10 > 9


# In[11]:


print(num)


# In[12]:


#string


# In[13]:


name = "abdullah"
len(name)


# In[18]:


name[2]    # index


# In[19]:


name[2] = 'd'  # strings are immutable means it cannot be changed


# In[20]:


name[2:8]


# In[21]:


name[-2]


# In[22]:


name.upper()


# In[23]:


#list


# In[136]:


mylist = [10, 20, 30, 30, "abdullah", "edureka"]


# In[137]:


mylist


# In[138]:


mylist[2]


# In[139]:


mylist[2:4]


# In[140]:


mylist[2] = "abdullah"


# In[141]:


mylist  # this shows that list are mutable


# In[142]:


mylist.append("kashif")


# In[143]:


mylist


# In[145]:


mylist.append("aamir")  # add value at the end


# In[37]:


mylist


# In[39]:


mylist.insert(2, "abid") # add value at specific place


# In[40]:


mylist


# In[42]:


mylist.reverse()


# In[43]:


mylist


# In[58]:


my_list = [2, 4, 1, 0, 6, 5, 3]


# In[59]:


sorted (my_list)


# In[60]:


my_list.reverse()


# In[61]:


my_list


# In[62]:


# Dictionary 


# In[63]:


courses = {1 : 'python', 2: 'data science', "third": 'machinelearning'}


# In[65]:


courses['third'] #here third , 1 , 2 are keys which can be duplicate


# In[71]:


courses[1]


# In[72]:


courses.get('third')


# In[73]:


courses['third']="hadoop"


# In[74]:


courses['third']


# In[75]:


courses['four'] = "machine learning"


# In[76]:


courses['four']


# In[77]:


courses


# In[78]:


#tuple is ordered and immutable


# In[79]:


animals = (10, 20, 30, "tiger", "lion", "tiger")


# In[80]:


animals[2]


# In[82]:


animals.count('tiger')


# In[84]:


# set (no duplicate values)


# In[87]:


myset = {10, 20, 30, 40, "edureka", "courses"}


# In[88]:


urset = {30, 40, "master", "data"}


# In[91]:


common = myset.intersection(urset)


# In[92]:


common


# In[93]:


total = myset.union(urset)


# In[94]:


total


# In[96]:


myset[2] # set doesnt support indexing


# In[97]:


#range


# In[98]:


range(10)


# In[99]:


list(range(11))


# In[100]:


#examples


# In[101]:


a = [1, 2, 3, 4]


# In[102]:


b = [4, 5, 6, 7, 8]


# In[103]:


c = [a, b]


# In[104]:


c


# In[108]:


c = [a+b] #concatenation


# In[109]:


c


# In[110]:


c = [a*b] # multiply nt allowed in list


# In[111]:


#type conversion


# In[112]:


str(x) + name


# In[113]:


list(b)


# In[114]:


# collections in python with modules


# In[115]:


#list = mutable
#tuples = immutable and ordered
#sets = immutable and cannot have duplicates and unordered
#dictionary = immutable and has key values


# In[116]:


#specialised collection data types


# In[117]:


#namedtuple()


# In[121]:


from collections import namedtuple
a = namedtuple('courses', 'name, technology')
s = a('data science', 'python')


# In[123]:


s = a._make(['artificial intelligence', 'python'])


# In[124]:


s


# In[125]:


#deque


# In[131]:


from collections import deque

a = ['e', 'd', 'u', 'r', 'e', 'k', 'a']
d = deque(a)
print(d)


# In[132]:


d.append('python')


# In[133]:


d


# In[134]:


d.appendleft('abdullah')  # left used with deque only


# In[135]:


d


# In[146]:


d.pop()
print(d)


# In[148]:


d.popleft()


# In[149]:


d


# In[150]:


#chainmap  it joins two dictionary


# In[151]:


from collections import ChainMap


# In[152]:


a1 = {1: 'edureka', 2: 'python'}
a2 = {3: 'ML', 4: 'AI'}


# In[158]:


c = ChainMap(a1, a2)


# In[159]:


print(c)


# In[160]:


#counter count hashable objects


# In[176]:


from collections import Counter


# In[177]:


a = [1, 1, 2, 3, 2, 2, 4, 5, 3, 5, 2, 2]
c = Counter(a)
c


# In[178]:


print(list(c.elements()))  #total number in sorted order


# In[179]:


print(c.most_common()) #how many times same number occur


# In[180]:


sub = {2:1 , 6:1}


# In[181]:


print(c.subtract(sub))
print(c.most_common())


# In[183]:


#Ordered dictionary it remember order in which object occured


# In[184]:


from collections import OrderedDict


# In[186]:


d = OrderedDict()
d[1] = 'e'
d[2] = 'd'
d[3] = 'u'
d[4] = 'r'
d[5] = 'e'
d[6] = 'k'
d[7] = 'a'
print(d)


# In[188]:


print(d.keys())


# In[189]:


print(d.items())


# In[190]:


print(d.values())


# In[191]:


d[1] = 'p'
d[4] = 'a'
d


# In[192]:


#default dict


# In[193]:


from collections import defaultdict


# In[194]:


d = defaultdict(int)
d[1] = 'python'
d[2] = 'edureka'
print(d[3])


# In[195]:


print(d[2])


# In[197]:


#Array , they are mutable


# In[198]:


import array as arr


# In[207]:


a = arr.array('f', [1, 2, 3, 4 ,5, 6])
a


# In[208]:


a[2]


# In[209]:


a.append(8)


# In[210]:


a


# In[211]:


a.extend([3.4, 3, 2])


# In[212]:


a


# In[213]:


a.insert(2, 4.6)


# In[214]:


a


# In[215]:


a.pop(2)


# In[216]:


a.remove(6)


# In[217]:


a


# In[219]:


a = arr.array('d', [2, 3, 4, 5, 6, 7]) 
b = arr.array('d', [])
c = arr.array('d', [3.4, 5.0])


# In[220]:


d = a+b+c #concatenation


# In[221]:


d


# In[223]:


print(d[2:5])


# In[224]:


d[-2]


# In[225]:


d[0:-2]


# In[226]:


d[::-1]


# In[227]:


#looping  for


# In[229]:


for x in d:    #it means go to every element(x) in a and print it
    print(x)


# In[230]:


for x in d[0:3]:
    print(x)


# In[231]:


#while loop 1. iteration, 2. to specify condition, 3. to increment iteration


# In[234]:


temp=0 #iterator
while temp < d[2]:
    
    print(d[temp])
    temp = temp+1


# In[236]:


tem = 0
while tem < len(a):
    print(a[tem])
    tem+=1


# In[237]:


#hash table and hashmap


# In[2]:


#creating dictionary two method


# In[3]:


#1


# In[48]:


my_dict = {'Dave : 001', 'Ava : 002'}


# In[49]:


print(my_dict)


# In[50]:


print(type(my_dict))


# In[51]:


#2


# In[52]:


new_dict = dict()
print(new_dict)
type(new_dict)


# In[53]:


new_dict = dict(Dave = '001', Ava ='0')
print(new_dict)


# In[2]:


#Nested Dictionaries


# In[3]:


emp_details = {'employee' : {'Dave':{'ID' : '001', 'Salary': '2000', 'Designation':'Team Lead'},
              'Ava':{'ID': '002', 'Salary': '3000', 'Designation' : 'Associate'}}}
               
                            


# In[4]:


print(emp_details)


# In[5]:


#performing operations on hash table


# In[6]:


#Accessing Items


# In[7]:


emp_details['employee']


# In[8]:


print(emp_details.keys())


# In[9]:


print(emp_details.values())


# In[10]:


print(emp_details.get('employee'))


# In[11]:


for x in emp_details.values():
    print(x)


# In[12]:


for x, y in emp_details.items():
    print(x, y)


# In[13]:


#Updating


# In[14]:


my_dict = {'Dave': '001', 'Eva': '002'}


# In[15]:


my_dict['Dave'] = '002'
my_dict['Chris']= '004'
print(my_dict)


# In[16]:


#Deleting Entries


# In[17]:


my_dict.pop('Chris')


# In[18]:


my_dict.popitem()


# In[20]:


#Pandas : making dataframe from nested dictionary


# In[19]:


import pandas as pd
df = pd.DataFrame(emp_details['employee'])
print(df)


# In[21]:





# In[ ]:




