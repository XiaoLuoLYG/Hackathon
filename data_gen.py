# user, date, in/out, type

import csv
import numpy as np
from datetime import date, timedelta


users = ['James']


income_type = ["Salary", "Investment", "Gift", "Other", "Youtube"]
expend_type = ["Food", "Shopping", "Transport",
               "Fitness", "Entertainment", "Social", "Travel"]


data = []

with open('data2.csv', 'w', newline='') as csvfile:
    moneywriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    moneywriter.writerow(['date', 'money', 'money_typ'])

    start_date = date(2017, 1, 1)   # start date
    end_date = date(2019, 12, 31)   # end date

    delta = end_date - start_date       # as timedelta

    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)

        money = np.random.normal(0,100)

        money_typ = None
        if (money > 0):
            money_typ = np.random.choice(income_type)
        elif (money < 0):
            money_typ = np.random.choice(expend_type)

        moneywriter.writerow([day, money, money_typ])
