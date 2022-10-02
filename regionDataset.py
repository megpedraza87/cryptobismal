#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 05:59:35 2022

@author: aarondelgado
"""

import pandas as pd
import matplotlib.pyplot as plt


      
df = pd.read_csv('every-20-rows-natality.csv')
df['County'].value_counts()
#print(df['County'].value_counts())

#changing datafeed to filter for only Texas
txdf = df[df["State"] == "Texas"]

plt.bar(txdf['County'].value_counts().index,txdf['County'].value_counts())
plt.xticks(rotation = 90)

#This data set shows the difference between different regions(counties)
#There is an obvious difference between some of the counties.







#for column in df.columns:
#    print(column)

