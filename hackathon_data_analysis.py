#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import os
import csv 
import datetime
from dateutil.relativedelta import relativedelta  
from datetime import datetime as dt


# In[9]:


filename = 'C:/Users/10513/Downloads/data2.csv'
data = pd.read_csv(filename)
print(data)


# In[10]:


"""
income_type = ["Salary", "Investment","Gift","Other","Youtube"]
expend_type = ["Food", "Shopping", "Transport", "Fitness", "Entertainment", "Social", "Travel"]


incomelist = []
expendlist = []
for i in range(1484):
    a = np.random.choice(income_type)
    incomelist.append(a)
    
for j in range(1484):
    b = np.random.choice(expend_type)
    expendlist.append(b)
    
print(len(incomelist))
"""


# In[11]:


"""# Use the multi-axes indexing funtion
data.insert(data.shape[1], 'Income type', incomelist)
data.insert(data.shape[1], 'Expend type', expendlist)"""


# In[12]:


print(data.head(10))


# In[13]:


data[data["date"]== '2018/1/1']


# In[14]:


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


# In[15]:


def get_time_month(y,m):
    date_list = []

    month_start_day = datetime.date(y, m, 1)
    month_start_day.isoformat()

    month_end_day = datetime.date(y, m+1, 1) - datetime.timedelta(days=1)
    month_end_day.isoformat()
    date_list = [month_start_day, month_end_day]
        
    return date_list


# In[16]:


def get_time_week(y,m,d):
    date_list = []
    if m < 10:
        a = "0"+"m"
    
        if d<10:
            b = "0"+"d"
        else:
            b = "d"
    else:
        b = "m"
    daystring = str(y)+str(m)+str(d)
    
    week=dt.strptime(daystring, "%Y%m%d").weekday()
    
    week_start_day = datetime.date(y, m, d)- datetime.timedelta(days=week)
    week_start_day.isoformat()

    week_end_day = datetime.date(y, m, d) + datetime.timedelta(days=6-week)
    week_end_day.isoformat()
    
    date_list = [week_start_day, week_end_day]
        
    return date_list


# In[17]:


def get_csv_data(date_list):
    start = str(date_list[0])
    end = str(date_list[1])
    s = data[data.date==start].index.tolist()
    e = data[data.date==end].index.tolist()
    d1 = s + e
    date_range = []
    for i in range(d1[0],d1[1]+1):
        date_range.append(i)
        
    csv_data = data.loc[date_range,:]
    return csv_data


# In[18]:


get_time_year(2018)
print(get_time_month(2018,2))
print(get_time_week(2018,12,3))


# In[19]:


date_list = get_time_week(2018,1,1)
d1 = get_csv_data(date_list)

print(d1)


# In[20]:


def get_type_sum(data):
    income_type = ["Salary", "Investment","Gift","Other","Youtube"]
    expend_type = ["Food", "Shopping", "Transport", "Fitness", "Entertainment", "Social", "Travel"]

    intypesum = {}
    extypesum = {}
    for i in income_type:
        intypesum[i]=data[data.money_typ == i].money.sum()

    for _ in expend_type:
        extypesum[_]=abs((data[data.money_typ == _]).money.sum())
        
    return intypesum, extypesum


# In[21]:


print(get_type_sum(d1))


# In[22]:


def get_income_sum(data):
    income_sum = data[data.money > 0].money.sum()
    return income_sum

print(get_income_sum(d1))


# In[23]:


def get_expend_sum(data):
    income_sum = abs(data[data.money < 0].money).sum()
    return income_sum

print(get_expend_sum(d1))


# In[ ]:




