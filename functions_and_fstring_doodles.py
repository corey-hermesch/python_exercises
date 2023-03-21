#!/usr/bin/env python
# coding: utf-8

# In[6]:


name = "Hello, World"


# In[23]:


f'{name.upper() : >20}!!!'


# In[24]:


f'{name.upper() : ^20}!!!'


# In[21]:


f"{(name.upper() + '!!!') : ^20}"


# In[28]:


f"{name.upper() : <20} {name.lower() : >20}"


# In[29]:


def do_this(a=7, b=21):
    return a+1, b-10


# In[30]:


do_this()


# In[31]:


do_this(5, 10)


# In[32]:


27 ** (1/3)


# In[33]:


16 ** .25


# In[34]:


plus_one = lambda n: n + 1


# In[36]:


plus_one(5)


# In[45]:


do_that = lambda x=1,y=2: (x+1, y-10)


# In[46]:


do_that(5,10)


# In[47]:


do_that()


# In[ ]:




