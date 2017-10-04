
# coding: utf-8

# In[6]:

import pandas as pd
dat=pd.read_csv("/Users/mariiashcherbiak/Downloads/BTS_MasterInBigData-master/Session_1/file_formats/rural_population_data.csv")


# In[7]:

dat.head()


# In[8]:

dat["Continent"].unique()


# In[10]:

dat["Growrate"]=(dat["Population2010"]-dat["Population2000"])/dat["Population2000"]


# In[11]:

dat.head()


# In[12]:

import matplotlib.pyplot as plt
dat["Growrate"].hist()


# In[13]:

dat.isnull().sum()


# In[20]:


dat["Average2000-2010"]=(dat["Population2000"]+dat["Population2010"])/2


# In[21]:

dat.head()


# In[23]:

count=0
for i in dat["UrbanRuralDesignation"]:
    if i=="Urban":
        count+=1
count
 


# In[ ]:




# In[ ]:



