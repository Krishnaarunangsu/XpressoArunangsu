# I have a pandas dataframe with few columns.
# Now I know that certain rows are outliers based on a certain column value.
# For instance columns - 'Vol' has all values around 12xx and one value is 4000 (Outlier).
# Now I would like to exclude those rows that have 'Vol' Column like this. So, essentially I need to put a filter on the data frame such that we select all rows where the values of a certain column are within say 3 standard deviations from mean.
# What is an elegant way to achieve this.
import numpy as np
import pandas as pd
import scipy
from scipy import stats
from scipy import optimize
print(np.)
# df = pd.DataFrame(np.random.randn(100, 3))
# x = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]
# print(df)
# print(x)

# description:
# For each column, first it computes the Z-score of each value in the column, relative to the column mean and standard deviation.
# Then is takes the absolute of Z-score because the direction does not matter, only if it is below the threshold.
# all(axis=1) ensures that for each row, all column satisfy the constraint.
# Finally, result of this condition is used to index the dataframe.
