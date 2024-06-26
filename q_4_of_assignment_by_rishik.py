# -*- coding: utf-8 -*-
"""Q.4 OF ASSIGNMENT BY RISHIK

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kd6ZrTyBBpK6B4MXLe2aXRLjyRx7Ian4
"""

import numpy as np
import pandas as pd

path=("/content/drive/MyDrive/DATASET/Groceries_dataset.csv")
df=pd.read_csv(path)
df.head()

df.isnull().sum()

x=df["itemDescription"].value_counts().sort_values(ascending=False)[:10]
x

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
df

df["Quantity"]=1
df

transactions=df.groupby(["Member_number","itemDescription"])["Quantity"].sum().unstack().reset_index().set_index("Member_number")

transactions=transactions.fillna(0)
transactions

# data got standardized
def encode(x):
  if x<=0:
    return 0
  elif x>=0:
    return 1
basket=transactions.applymap(encode)
basket

# (A) part
frequent_itemset = apriori(basket,min_support=0.06,use_colnames=True)
rules=association_rules(frequent_itemset,metric="lift",min_threshold=1)
rules.head()

rules[(rules["confidence"]>0.4)]

# (B) part
frequent_itemset = apriori(basket,min_support=0.05,use_colnames=True)
rules1=association_rules(frequent_itemset,metric="lift",min_threshold=1)
rules1.head()

rules1[(rules["confidence"]>0.075)]