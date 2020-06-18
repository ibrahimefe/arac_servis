# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:46:49 2020

@author: ibrah
"""

import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv("dummyDataset20200617_150932.csv")
df.drop(["plaka","marka","model","uretim_tarihi","tarih","parca_fiyat"],axis =1, inplace=True)
test = (df.iloc[1000:1110,0].values).reshape(-1,1)
df.drop(df.loc[1000:24000].index, inplace=True)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
x=df.km.values.reshape(-1,1)
y=df.iscilik_fiyat.values.reshape(-1,1)
lr.fit(x,y)
y_head = lr.predict(test)
plt.plot(test, y_head, color="red")
plt.scatter(df.km,df.iscilik_fiyat)
plt.xlabel("km")
plt.ylabel("İscilik Fiyatı")
plt.show()


