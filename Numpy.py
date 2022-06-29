#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


a = ([[1,6],
      [2,8],
      [3,11],
      [3,10], 
      [1,7]])


# In[4]:


mean_a = np.mean(a, axis = 0)


# In[5]:


mean_a


# In[6]:


a_centered = np.subtract(a, mean_a)


# In[7]:


a_centered = a - mean_a


# In[8]:


a_centered


# In[9]:


np.shape(a_centered)


# In[12]:


a_1 = a_centered[:,0]


# In[13]:


a_2 = a_centered[:,1]


# In[14]:


a_centered_sp = np.dot(a_1, a_2)


# In[15]:


a_centered_sp


# In[21]:


N = a_centered.shape[0]


# In[23]:


q = a_centered_sp / (N - 1)


# In[24]:


q

