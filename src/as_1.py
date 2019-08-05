import pandas as pd
import numpy as np
# https://pbpython.com/pandas-list-dict.html


# df = pd.DataFrame(calculation)
df = pd.read_csv('../data/anushree_testcase_2.csv')
print(df)
bins = 100
# df['binned'] = pd.cut(df['percentage'], bins)
pdf = pd.cut(df, bins).count()
print(pdf)

# Perform a shape check on the DataFrame
# ValueError: Buffer has wrong number of dimensions (expected 1, got 2)
