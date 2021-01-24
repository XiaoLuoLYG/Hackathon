#!/usr/bin/env python
# coding: utf-8

# In[178]:


import pandas as pd
import numpy as np
import os
import csv 
import datetime
from dateutil.relativedelta import relativedelta  
from datetime import datetime as dt
from pandas import DataFrame
import plotly.express as px
import plotly.graph_objects as go
import plotly


# In[179]:


#Fetch the file
filename = './export.csv'
#filename = 'C:/Users/10513/Downloads/data2.csv'
data = pd.read_csv(filename)
print(data.head(10))


# In[180]:


#datefile = './instructions.csv'
#date_data = pd.read_csv(datefile)
date_data = DataFrame({'date':['2019-11-01'],'type':[2]})
print(date_data)


# In[181]:


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

def get_time_month(y,m):
    date_list = []

    month_start_day = datetime.date(y, m, 1)
    month_start_day.isoformat()

    month_end_day = datetime.date(y, m+1, 1) - datetime.timedelta(days=1)
    month_end_day.isoformat()
    date_list = [month_start_day, month_end_day]
        
    return date_list

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

def get_time_range(date_data):
    datedate = date_data.date.tolist()
    datestring = str(datedate[0])
    x = datestring.split('-')
    datetype = date_data.type.tolist()

    if datetype[0] == 0:
        year = int(x[0])
        month = int(x[1])
        day = int(x[2])
        date_list = get_time_week(year,month,day)

    if datetype[0] == 1:
        year = int(x[0])
        month = int(x[1])
        date_list = get_time_month(year,month)

    if datetype[0] == 2:
        year = int(x[0])
        date_list = get_time_year(year)
        
    return date_list



# In[182]:


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


# In[183]:


print(get_time_year(2018))
print(get_time_month(2018,2))
print(get_time_week(2018,12,3))


# In[184]:


date_list = get_time_range(date_data)
d1 = get_csv_data(date_list)

print(d1)


# In[185]:


def get_type_sum(data):
    income_type = ["Salary", "Investment","Gift","Other","Youtube"]
    expend_type = ["Food", "Shopping", "Transport", "Fitness", "Entertainment", "Social", "Travel"]

    intypesum = {}
    extypesum = {}
    for i in income_type:
        intypesum[i]=data[data.money_typ == i].money.sum()

    for _ in expend_type:
        extypesum[_]=abs((data[data.money_typ == _]).money.sum())
        
    return [intypesum, extypesum]


# In[186]:


#Dataframe for plotting
income_type_sum = get_type_sum(d1)[0]

items=income_type_sum.items()
keys = []
values = []
for item in items:
    key=item[0]
    value=item[1]
    keys.append(key)
    values.append(value)
    
print(keys)
print(values)
income_type_data = {'Type':keys, 'Sum':values}
dfin = DataFrame(income_type_data)
print(dfin)


# In[187]:


expend_type_sum = get_type_sum(d1)[1]

items=expend_type_sum.items()
keys = []
values = []
for item in items:
    key=item[0]
    value=item[1]
    keys.append(key)
    values.append(value)
    
print(keys)
print(values)
expend_type_data = {'Type':keys, 'Sum':values}
dfex = DataFrame(expend_type_data)
print(dfex)


# In[188]:


def get_income_sum(data):
    income_sum = data[data.money > 0].money.sum()
    return income_sum

print(get_income_sum(d1))


# In[189]:


def get_expend_sum(data):
    income_sum = abs(data[data.money < 0].money).sum()
    return income_sum

print(get_expend_sum(d1))


# In[190]:


fig = px.pie(dfex, values='Sum', names='Type')
fig.update_traces(textposition='inside')
fig.write_image('./d1expie.jpg')
fig.show()


# In[191]:


fig = px.pie(dfin, values='Sum', names='Type')
fig.update_traces(textposition='inside')
fig.write_image('./d1inpie.jpg')
fig.show()


# In[192]:


#df = px.data.d1()
fig = px.line(d1, x='date', y="money")
fig.write_image('./data2.jpg')
fig.show()


# In[193]:


fig = px.line(d1[d1.money > 0], x='date', y="money")
fig.write_image('./income.jpg')
fig.show()


# In[194]:


fig = px.line(d1[d1.money < 0], x='date', y="money")
fig.write_image('./expend.jpg')
fig.show()


# In[195]:


insum = get_income_sum(d1)
exsum = get_expend_sum(d1)
keys = ['Income', 'Expenditure']
values = [insum, exsum]
in_and_ex = {'':keys, 'Sum':values}
dff = DataFrame(in_and_ex)

fig = px.bar(dff,x='', y='Sum')
fig.write_image('./d1bar.jpg')
fig.show()


# In[ ]:




