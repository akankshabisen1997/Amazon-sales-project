#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset=pd.read_csv('Amazon Sales data 2.csv')
dataset


# In[2]:


dataset.head()


# In[19]:


dataset.tail()


# In[4]:


dataset.isnull().sum()


# In[5]:


dataset.dtypes


# In[6]:


dataset.columns


# In[7]:


dataset.shape


# # Item Type

# In[115]:


plt.figure(figsize=(9,5))
sns.countplot(x='Item Type',data=dataset)
plt.xticks(rotation=20)
plt.xlabel('Item Type',fontsize=19)
plt.ylabel('Count',fontsize=19)
plt.title('Count of Item Type')
plt.savefig('Count of Item Type.jpg')
plt.show()


# In[ ]:


#From above graph we can see that Cloths and Cosmetics Item are purchase as compare other Item type. 


# In[95]:


dataset['Item Type'].value_counts()


# In[9]:


dataset['Item Type'].unique()


# In[117]:


plt.figure(figsize=(10,5))
sns.countplot(x='Item Type',data=dataset,hue='Sales Channel',palette='RdBu',saturation=20)
plt.title('Count of Item Type',fontsize=15)
plt.xticks(rotation=20)
plt.xlabel('Item Type',fontsize=19)
plt.ylabel('Count',fontsize=19)
plt.show()


# In[ ]:


From above  graph we can see the payment Type is online.


# # Order Priority

# In[62]:


dataset['Order Priority'].value_counts()


# In[74]:


x =dataset['Order Priority'].value_counts().index
y =dataset['Order Priority'].value_counts().values


# In[84]:


plt.figure(figsize=(5,4))
plt.pie(y,labels=x,startangle=50,autopct="%0.2f%%",shadow=True)
plt.legend(loc=2)
plt.title('pie chart')
plt.show()


# In[ ]:


From above graph we can see the percentage of order priority in H.


# # Total Profit

# In[112]:


plt.figure(figsize=(9,5))
sns.barplot(x='Item Type',y='Total Profit',data=dataset,estimator='sum')
plt.xticks(rotation=20)
plt.xlabel('Item Type',fontsize=19)
plt.ylabel('Count',fontsize=19)
plt.show()

# From the above graph we can see the total profit is comes from cosmetic kind of Item.
# # Region wise Profit

# In[114]:


dataset['Region'].value_counts()


# In[ ]:


From  the above data  we can see that unexpectedly most of the Items sold are From 
Sub-Saharan Africa,Europe,Australia,Oceania respectively.
   


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




