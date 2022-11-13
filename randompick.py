#!/usr/bin/env python
#coding:utf-8

import sys
import datetime
import random
import twstock
#import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
mpl.rcParams[u'font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False

month = 1

if len(sys.argv) > 2:
    stock_code = sys.argv[1]
    month = int(sys.argv[2])
elif len(sys.argv) == 2:
    stock_code = sys.argv[1]
else:
    while 1:
        stock_code = random.randint(1000, 9999)
        if str(stock_code) in twstock.twse:
            break


today = datetime.date.today()
#target_date = today.replace(month = (today.month - month))
target_date = today - datetime.timedelta(days=(month *30))

stock = twstock.Stock(str(stock_code))
if month == 1:
    stock_data = stock.fetch_31()
else:
    stock_data = stock.fetch_from(target_date.year, target_date.month)

#print(stock_data)
stock_pd = pd.DataFrame(stock_data)
#print(stock_pd)
stock_pd = stock_pd.set_index('date')
stock_name = twstock.codes[stock.sid].name

print("Pick: ", stock.sid)
print(today)
print(target_date)
print(len(stock.price), " days data")
#print(stock)


fig = plt.figure(figsize=(10, 6))
plt.plot(stock_pd.close, '-' , label="收盤價")
plt.plot(stock_pd.open, '-' , label="開盤價")
plt.title(stock_name + ' 開盤/收盤價曲線',loc='right')
# loc->title的位置
plt.xlabel('日期')
plt.ylabel('收盤價')
plt.grid(True, axis='y')
plt.legend()
to_str = today.strftime('%Y%m%d')
from_str = target_date.strftime('%Y%m%d')

fig.savefig(stock_name + '-' + to_str + '-' + from_str + '.png')
