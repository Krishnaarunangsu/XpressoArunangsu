import pandas as pd
import numpy as np

# Discretize into three equal-sized bins
result_1 = pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3)
print(result_1)
print('************************************************************')
result_2 = pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3, retbins=True)
print(result_2)
print('************************************************************')

# Discovers the same bins, but assign them specific labels.
# Notice that the returned Categorical’s categories are labels and is ordered.
result_3 = pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3, labels=["bad", "medium", "good"])
print(result_3)
print('************************************************************')

result_4 = pd.cut([0, 1, 1, 2], bins=4, labels=False)
print(result_4)
print('************************************************************')

# Passing a Series as an input returns a Series with mapping value.
# It is used to map numerically to intervals based on bins.
s = pd.Series(np.array([2, 4, 6, 8, 10]),
               index=['a', 'b', 'c', 'd', 'e'])
result_5 = pd.cut(s, [0, 2, 4, 6, 8, 10], labels=False, retbins=True, right=False)
print(result_5)
print('************************************************************')

# Use drop optional when bins is not unique
result_6 = pd.cut(s, [0, 2, 4, 6, 8, 10], labels=False, retbins=True, right=False, duplicates='drop')
print(result_6)
print('************************************************************')

# Passing an IntervalIndex for bins results in those categories exactly.
# Notice that values not covered by the IntervalIndex are set to NaN.
# 0 is to the left of the first bin (which is closed on the right),
# and 1.5 falls between two bins.
bins = pd.IntervalIndex.from_tuples([(0, 1), (2, 3), (4, 5)])
result_7 = pd.cut([0, 0.5, 1.5, 2.5, 4.5], bins)
print(result_7)