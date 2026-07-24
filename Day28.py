from datetime import datetime,date,time
current=datetime.now()
today=date.today()
now=datetime.now()
print(current)
print(current.strftime('%y'))
print(current.strftime('%m'))
print(current.strftime('%d'))
print(current.strftime('%d'))
print(today,now)
print(current.strftime('%d/%m/%y  %H:%M:%S %p'))#if 24hrs %I
import calendar
print(calendar.calendar(2026))
print(calendar.month(2026,7))
print(calendar.weekday(2026,7,24))
print(calendar.isleap(2024))
""" data anaysis

Descriptive Analysis: Summarizes past data to show what happened.
Diagnostic Analysis: Explores data deeper to find why something happened.
Predictive Analysis: Uses historical trends to forecast what might happen next.
Prescriptive Analysis: Recommends specific actions based on insights.

NumPy Array Types
1D Arrays (Vectors): A single row of homogeneous elements.
2D Arrays (Matrices): Data structured strictly in rows and columns.
3D+ Arrays (Tensors):Multi-dimensional structures for complex or volumetric
"""
import numpy as np
a=np.array([1,2,3,4])
print(a.sum())
print(a.mean())
print(a.max())
print(a.min())
a=np.array([[1,2,3,4],[5,5,6,7],[7,8,9,10]])
print(a)
print(a.reshape(4,3))

import pandas as pd
data=pd.Series([2000,4000,7000],index=['earphones','charger','mobile'])
print(data)
df={"product":['laptop','charger','mobile'],
    "brand":['mac','realme','iphone'],
    'price':[5700,1500,2500],
    'stocks':[5,15,9],
    'sales':['amozon','offline','filpkart']
    }
data=pd.DataFrame(df)
print(data)
