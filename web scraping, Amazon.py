#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install request


# In[2]:


pip install bs4


# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[4]:


url="https://www.amazon.nl/s?k=mobile+samsung&language=en_GB&__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3RSZ462GGZJES&sprefix=mobile+samsung%2Caps%2C75&ref=nb_sb_noss_1"


# In[5]:


site = requests.get(url)


# In[6]:


soup = BeautifulSoup(site.text, 'html.parser')


# In[15]:


soup


# In[7]:


X= soup.find("div", {"class":"s-main-slot s-result-list s-search-results sg-row"})
X


# In[8]:


X2=X.find_all("span", {"class": "a-size-base-plus a-color-base a-text-normal"})
X2


# In[ ]:


len(X2)


# In[ ]:


Title=[]
for i in range (48):
    Title.append(X2[i])


# In[ ]:


Title


# In[ ]:


df= pd.DataFrame(Title)


# In[ ]:


df


# In[ ]:


#df.to_excel("Samsung.xlsx")


# In[ ]:


import os


# In[ ]:


os.getcwd()


# In[ ]:


X3=X.find_all("span", {"class": "a-price-whole"})
X3


# In[ ]:


len(X3)


# In[ ]:


Price=[]
for i in range (35):
    Price.append(X3[i])


# In[ ]:




