import pandas as pd
import numpy as np

# Create a DataFrame
df1 = {
    'Name': ['George', 'Andrea', 'micheal', 'maggie', 'Ravi', 'Xien', 'Jalpa', 'Tyieren'],
    'Score': [63, 48, 56, 75, 32, 77, 85, 22]
}

df1 = pd.DataFrame(df1, columns=['Name', 'Score'])
print(df1)

''' binning or bucketing with range values'''

# bins = [0, 25, 50, 75, 100]
bins = 100
df1['binned'] = pd.cut(df1['Score'], bins)
print(df1)

''' binning or bucketing with labels'''

bins = [0, 25, 50, 75, 100]
labels = [1, 2, 3, 4]
df1['binned'] = pd.cut(df1['Score'], bins, labels=labels)
print(df1)

# http://www.datasciencemadesimple.com/binning-or-bucketing-of-column-in-pandas-python-2/