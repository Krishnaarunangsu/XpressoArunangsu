import pandas as pd
import numpy as np
# https://pbpython.com/pandas-list-dict.html

calculation = [{'percentage': 15},
               {'percentage': 12},
               {'percentage': 17},
               {'percentage': 19},
               {'percentage': 10},
               {'percentage': 16},
               {'percentage': 11},
               {'percentage': 18},
               {'percentage': 14}]
df = pd.DataFrame(calculation)
bins = [0, 1, 5, 10, 25, 50, 100]
df['binned'] = pd.cut(df['percentage'], bins)
print(df)


bins = [0, 1, 5, 10, 25, 50, 100]
labels = [1, 2, 3, 4, 5, 6]
df['binned'] = pd.cut(df['percentage'], bins=bins, labels=labels)
print(df)

# Or numpy.searchsorted:
bins = [0, 1, 5, 10, 25, 50, 100]
df['binned'] = np.searchsorted(bins, df['percentage'].values)
print(df)

# and then value_counts or groupby and aggregate size:
s = pd.cut(df['percentage'], bins=bins).value_counts()
print(s)

s = df.groupby(pd.cut(df['percentage'], bins=bins)).size()
print(s)

# By default cut return categorical.
#
# Series methods like Series.value_counts() will use all categories,
# even if some categories are not present in the data, operations in categorical.
