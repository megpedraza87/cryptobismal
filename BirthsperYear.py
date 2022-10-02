# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 03:57:45 2022

@author: meglo
"""

# download and print first 5 lines of file
import pandas as pd
df = pd.read_csv("every-20-rows-natality.csv")
print(df.head())

# changing datafeed to filter for only Texas births
txdf = df[df["State"] == "Texas"]
print(txdf.head())

# printing the total count per year
print(txdf['DT_YEAR'].value_counts().sort_index()*20)

# plotting each count on line graph with labels
import matplotlib.pyplot as plt
plt.plot(txdf['DT_YEAR'].value_counts().sort_index()*20)
plt.ylabel("# of Births (in thousands)")
plt.xlabel('Years')
plt.title("Births Per Year")

# data shows that birth rate was low until 1975 when there is a 28% increase 
# in births, which then continued to climb higher each year.