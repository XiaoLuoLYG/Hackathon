#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd
import numpy as np
import os
import csv 
import datetime
from dateutil.relativedelta import relativedelta  


# In[90]:


filename = 'C:/Users/10513/OneDrive/Documents/Cam/testdata.csv'
data = pd.read_csv(filename)
print(data)


# In[91]:



income_type = ["Salary", "Investment","Gift","Other","Youtube"]
expend_type = ["Food", "Shopping", "Transport", "Fitness", "Entertainment", "Social", "Travel", "Other"]


incomelist = []
expendlist = []
for i in range(1484):
    a = np.random.choice(income_type)
    incomelist.append(a)
    
for j in range(1484):
    b = np.random.choice(expend_type)
    expendlist.append(b)
    
print(len(incomelist))


# In[92]:


# Use the multi-axes indexing funtion
data.insert(data.shape[1], 'Income type', incomelist)
data.insert(data.shape[1], 'Expend type', expendlist)


# In[94]:


print(data.head(10))


# In[95]:


data[data["Date"]== '2018/1/1']


# In[ ]:


def tips():
    pass


# In[25]:


today = datetime.date.today()
print(today)

last_2_month = today + relativedelta(months=-2)  
print(last_2_month)
def get_time_week():
    
    today = datetime.date.today()
    
    week_start_day = today - datetime.timedelta(days=today.weekday())
    week_start_day.isoformat() 

    week_end_day = today + datetime.timedelta(days=6-today.weekday())
    week_end_day.isoformat()    
    
    pass
    
def get_csv_data():
    pass


# In[44]:



def get_time_year(n):
    date_list = []
    if n == 2021:
        today = datetime.date.today()

        year_start_day = datetime.date(today.year, 1, 1)
        year_start_day.isoformat()
        
        year_end_day = today
        
        date_list = [year_start_day, year_end_day]
        
    else:
        year_start_day = datetime.date(n, 1, 1)
        year_start_day.isoformat()
        
        year_end_day = datetime.date(n+1, 1, 1) - datetime.timedelta(days=1)
        year_end_day.isoformat()
        date_list = [year_start_day, year_end_day]
    return date_list


# In[47]:


get_time_year(2018)


# In[52]:


date_list = get_time_year(2018)
start = str(date_list[0])
type(start)
data[data[Date] == start]


# In[38]:


today = datetime.date.today()
year_start_day = datetime.date(2019, 12, 31)
year_start_day.isoformat()
print(year_start_day)


# In[ ]:


#dataset

expend = []
income = []

