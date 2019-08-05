# Groupby count in pandas dataframe python
# Groupby count in pandas python can be accomplished by groupby() function. let’s see how to
# Groupby single column in pandas – groupby count
# Groupby multiple columns in pandas – groupby count
# First let’s create a dataframe


import pandas as pd
import numpy as np

data = {'Name':['James','Paul','Richards','Marico','Samantha','Ravi','Raghu','Richards','George','Ema','Samantha','Catherine'],
       'State':['Alaska','California','Texas','North Carolina','California','Texas','Alaska','Texas','North Carolina','Alaska','California','Texas'],
       'Sales':[14,24,31,12,13,7,9,31,18,16,18,14]}

df1=pd.DataFrame(data, columns=['Name','State','Sales'])
print(df1)

# Groupby single column – groupby count pandas python:
''' Group by single column in pandas python'''
df2 = df1.groupby(['State'])['Sales'].count()
print(df2)

# Groupby multiple columns – groupby count pandas python:
''' Group by multiple columns

We will groupby count with State and Name columns, so the result will be

'''
df3 = df1.groupby(['State','Name'])['Sales'].count()
print(df3)

