#!/usr/bin/env python
#coding:utf-8

import random
import twstock
#import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
mpl.rcParams[u'font.sans-serif'] = ['simhei']
mpl.rcParams['axes.unicode_minus'] = False

found = 0
while 1:
    stock_code = random.randint(1000, 9999)
    if str(stock_code) in twstock.twse:
        break
    
stock = twstock.Stock(str(stock_code))
stock_data = stock.fetch_31()
#print(stock_data)
stock_pd = pd.DataFrame(stock_data)
#print(stock_pd)
stock_pd = stock_pd.set_index('date')
print("Pick: ", stock.sid)
stock_name = twstock.codes[stock.sid].name
print(len(stock.price), " days data")
print(stock)


fig = plt.figure(figsize=(10, 6))
plt.plot(stock_pd.close, '-' , label="收盤價")
plt.plot(stock_pd.open, '-' , label="開盤價")
plt.title(stock_name + ' 開盤/收盤價曲線',loc='right')
# loc->title的位置
plt.xlabel('日期')
plt.ylabel('收盤價')
plt.grid(True, axis='y')
plt.legend()
fig.savefig('day20_01.png')
