#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


authors = pd.DataFrame({'author_id':[1,2,3],
                       'author_name':['Тургенев','Чехов','Островский']},
                      columns = ['author_id', 'author_name'])


# In[4]:


print(authors)


# In[5]:


book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                    'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                    'price':[450, 300, 350, 500, 450, 370, 290]},
                      columns = ['author_id', 'book_title','price'])


# In[6]:


print(book)


# In[7]:


authors_price = pd.merge(authors, book, on = 'author_id')


# In[8]:


print(authors_price)


# In[10]:


top5 = authors_price.nlargest(5, 'price')


# In[11]:


print(top5)


# In[12]:


authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})


# In[13]:


authors_stat = authors_stat.rename(columns = {'min':'min_price', 'max':'max_price', 'mean':'mean_price'})


# In[14]:


print(authors_stat)


# In[ ]:





# In[ ]:




