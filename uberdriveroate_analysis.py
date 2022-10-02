#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_palette("deep")
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


uber_drives = pd.read_csv('uberdrive.csv')                  
uber_drives


# In[6]:


uber_drives.head()


# In[7]:


uber_drives.shape


# In[ ]:


# total number or rows are 1155 and number of columns are 7.


# In[8]:


uber_drives.size # total n0. of elements


# In[9]:


uber_drives.info()


# In[10]:


uber_drives.isnull().any().any()


# In[11]:


uber_drives.isnull().sum()


# In[12]:


uber_drives.describe()


# In[13]:


df=uber_drives.dropna()
df


# In[14]:


df.info()


# In[15]:


#Get the unique start locations.
df.columns


# In[16]:


df["START*"].unique()


# In[18]:


# total number of unique start destinations
print("the Total number of unique  start  locations are",uber_drives["START*"].nunique())


# In[21]:


#the total number of unique stop locations
print("the Total number of unique  stop  locations are",uber_drives["STOP*"].nunique())
      


# In[22]:


#Display all Uber trips that has the starting point as San Francisco
uber_drives.loc[uber_drives["START*"] == "San Francisco"]


# In[23]:


#the most popular starting point for the Uber drivers
uber_drives["START*"].value_counts().max


# In[ ]:


#so,the most popular starting point is Cary with 201 times


# In[24]:


#finding the most popular dropping point for the Uber drivers
uber_drives["STOP*"].value_counts().max


# In[ ]:


#the most popular droping point is Cary with 203 Times


# In[25]:


#finding the most frequent route taken by Uber drivers
df['START*'].value_counts()


# In[26]:


df['STOP*'].value_counts()


# In[27]:


freq = df.groupby(["START*","STOP*"]).sum()
freq


# In[ ]:


#Most popular start and end point is Cary so the Most frequent route taken by Uber drivers is"apex" to "Cary"


# In[28]:


#Displaying all types of purposes for the trip in an array
df["PURPOSE*"].unique()


# In[29]:


#Plot a bar graph of Purpose vs Miles(Distance).
uber_drives.head()


# In[30]:


uber_drives1 = uber_drives.fillna('Not Mentioned ')
uber_drives1


# In[ ]:


# uber_drives1 has no "na" values.


# In[31]:


ud = uber_drives1.groupby(['CATEGORY*','PURPOSE*']).sum()
ud


# In[32]:


type(ud)


# In[33]:


ud.columns


# In[34]:


type(ud.columns)


# In[36]:


plt.figure(figsize = (8,6))
ud['MILES*'].plot( kind= 'bar' )
plt.show()


# In[37]:


#Displaying a dataframe of Purpose and the total distance travelled for that particular Purpose
uber_drives.head()


# In[38]:


uber_drives1 = uber_drives.fillna('Not Mentioned ')
uber_drives1


# In[39]:


uber_drives1.groupby(['PURPOSE*']).sum()


# In[40]:


uber_drives['MILES*'].sum()


# In[41]:


uber_drives1['MILES*'].sum()


# In[42]:


df['MILES*'].sum()


# In[44]:


#Generate a plot showing count of trips vs category of trips
  #number of trips per category
uber_drives['CATEGORY*'].value_counts()  


# In[46]:


plt.figure(figsize = (5,5))
sns.countplot(x = "CATEGORY*", data = uber_drives)
plt.show()


# In[47]:


plt.figure(figsize = (15,5))
sns.countplot(x = "PURPOSE*", data = uber_drives)
plt.show()


# In[48]:


#percentage of Miles were clocked under Business Category and what percentage of Miles were clocked under Personal Category
uber_drives.head()


# In[49]:


uber_drives["CATEGORY*"].unique()


# In[50]:


uber_drives["CATEGORY*"].value_counts()


# In[51]:


#Proportion calculation is with respect to the 'miles' variable.
uber_drives['MILES*'].sum()


# In[52]:


ub = uber_drives.groupby(['CATEGORY*','PURPOSE*']).sum()
ub


# In[53]:


total_miles=uber_drives['MILES*'].sum()
total_miles


# In[54]:


business = 16.5+197+2089.5+508+911.7+2851.3+4389.3+523.7 
business


# In[55]:


personal = 15.1+180.2+18.2+504.2
personal


# In[56]:


total = business+personal
total


# In[57]:


print("Percentage of Business",(business/total)*100 )


# In[58]:


print("Percentage of Personal",(personal/total)*100 )


# In[ ]:




