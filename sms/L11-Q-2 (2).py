# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 09:36:56 2024

@author: Sanam Sadat Nikkhah

subject=Q-L11
"""

import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

a = random.uniform(0, 100)

b = random.gauss(7, 27)

c = np.random.randint(0, 200, size=5)

d = np.random.randint(0, 200, size=(2, 5))
plt.hist(d)

e = np.random.normal(loc=7, scale=2, size=(200))
plt.hist(e)

f = np.random.uniform(200)
plt.hist(f)

g = pd.Series([1, 3, 5, 7, 9])

h = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])

i = pd.DataFrame([[3, 5, 9], [2, 4, 8]])

i = pd.DataFrame([[3, 5, 9], [2, 4, 8]], columns=['Velocity', 'Temperature', 'Pressure'])

'''Question:
    Why isn't this code valid?
    i=pd.DataFrame ( [[3,5,9] , [2,4,8]],  columns=['Velocity', 'Temperature', 'Pressure']index=["Sample1", "Sample2", "Samle3"])
'''

j = np.array([[3, 5, 9], [2, 4, 8]])
data = pd.DataFrame(j, columns=['Velocity', 'Temperature', 'Pressure'])

'''Question:
    How can I fix this?

    k=data.iloc[2]
    print(k)
    L=data.loc[2]
    print(L)

    IndexError: single positional indexer is out-of-bounds
'''

data['Velocity']

data[['Velocity', 'Temperature']]

m = pd.DataFrame([1, 2])
n = pd.DataFrame([3, 4])
o = n + m

p = data.max()
q = data.max(axis=0)
r = data.max(axis=1)
#axis=0 : satr

print(p)
print(q)
print(r)

s = data['Velocity'].max()
print(s)

t = data.sort_values(by='Velocity')
print(t)

'''Question:
    
    What does sorting by 'Velocity'' mean? What does it exactly do?
    
'''

m = pd.DataFrame([1, 2])
n = pd.DataFrame([3, 4])
o = pd.concat([m, n])
print(o)

'''Question:
    
    Why is the result displayed like this?
    
    print(0):
        0
     0  1
     1  2
     0  3
     1  4
'''

Data = pd.DataFrame([[3, 5, 9], [2, 4, 8]], columns=['Velocity', 'Temperature', 'Pressure'])
'''
a=Data.drop(columns= 'Velocity')
print(a)
'''
b = Data.drop(columns='Velocity', inplace=True)
print(b)
Data.reset_index(drop=True, inplace=True)
print(Data)

import pandas as pd

dataframe = pd.read_excel("C:/Users/ASUS/Desktop/NullGeomembrane PE-Tensile Test D6693.xlsx")
print(dataframe)
'''
   Test No.  Thickness mm  ...  Strain at Break %  Stress at Break kN/m
   Unnamed: 0  Thickness mm  ...  Strain at Break %  Stress at Break kN/m
0         NaN          1.51  ...             729.91                 43.96
1         NaN          1.66  ...             752.17                 48.65
2         NaN          1.77  ...             756.91                 50.11
3         NaN          1.73  ...             708.38                 49.84
4         NaN           NaN  ...                NaN                   NaN
5         NaN         48.37  ...              48.37                 48.37

[6 rows x 7 columns]
'''

dataframe.head()
dataframe.head(3)
'''
   Unnamed: 0  Thickness mm  ...  Strain at Break %  Stress at Break kN/m
0         NaN          1.51  ...             729.91                 43.96
1         NaN          1.66  ...             752.17                 48.65
2         NaN          1.77  ...             756.91                 50.11

[3 rows x 7 columns]
'''
dataframe.tail()
dataframe.tail(3)
'''
   Unnamed: 0  Thickness mm  ...  Strain at Break %  Stress at Break kN/m
3         NaN          1.73  ...             708.38                 49.84
4         NaN           NaN  ...                NaN                   NaN
5         NaN         48.37  ...              48.37                 48.37

[3 rows x 7 columns]
'''

dataframe = pd.read_excel("C:/Users/ASUS/Documents/codes/Spyder(python)/NullGeomembrane PE-Tensile Test D6693.xlsx")

dataframe.info()

'''
dataframe.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 7 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   Unnamed: 0            0 non-null      float64
 1   Thickness mm          5 non-null      float64
 2   width mm              5 non-null      float64
 3   Strain at Yield %     5 non-null      float64
 4   Stress at Yield kN/m  5 non-null      float64
 5   Strain at Break %     5 non-null      float64
 6   Stress at Break kN/m  5 non-null      float64
dtypes: float64(7)
memory usage: 468.0 bytes
'''

dataframe = pd.read_excel("C:/Users/ASUS/Documents/codes/Spyder(python)/NullGeomembrane PE-Tensile Test D6693.xlsx")

#dataframe.dropna(inplace=True)
print(dataframe)
dataframe['Thickness mm'] = dataframe['Thickness mm'].fillna(0, inplace=True)
#dataframe.fillna(0,inplace=True)
dataframe['Thickness mm'] = dataframe['Thickness mm'].fillna(0, inplace=True)
print(dataframe)

i = dataframe['Thickness mm'].mean()
dataframe['Thickness mm'].fillna(a, inplace=True)
print(dataframe)
'''
dataframe['Thickness mm'].fillna(0,inplace=True):
    
FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.

'''
dataframe.fillna(method='ffill', inplace=True)
dataframe.fillna(method='bfill', inplace=True)

import pandas as pd

MyNumbers = pd.Series(['1.1', 2, '3', 4])

ConvertedToFloat = pd.to_numeric(MyNumbers, downcast='float')
ConvertedToFloat = pd.to_numeric(MyNumbers, downcast='int')

'''Question???
ValueError: invalid downcasting method provided

'''
import pandas as pd

MyDates = pd.Series(['24-6-8', 23 - 6 - 8, '24-6-8', 2024 - 6 - 8])
ConvertedToDate = pd.to_datetime(MyDates)

for i in dataframe:
    if dataframe.loc["Thickness mm"] < 3.4:
        dataframe.loc["Thickness mm"] = 3.4

dataframe.reset_index()
