import pandas as pd
import numpy as np
# https://pbpython.com/pandas-list-dict.html


df = pd.read_csv('../data/anushree_testcase_2.csv')
print(df)

df['Age_Bin'] = pd.cut(df['Age'], 4)
print(df)

df_1 = df[['Age','Age_Bin']].groupby(['Age_Bin']).agg(['mean', 'count'])
print(df_1)


count_pcts = df_1.groupby(['Age_Bin']).apply(lambda x:
                                                 100 * x / float(x.sum()))
