#!/usr/bin/env python
# coding: utf-8

# In[1]:


def check(word):
    if word == word[: : -1]:
        return True
    else:
        return False


# In[4]:


def add(*n):
    s = 0
    for i in n :
        s += i
    return s


# In[ ]:




