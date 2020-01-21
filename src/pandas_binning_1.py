# https://dfrieds.com/data-analysis/bin-values-python-pandas
# Data Analysis Data Wrangling Tutorial
# cut() Method: Bin Values into Discrete Intervals

# Import Modules
import pandas as pd
import numpy as np
# Why Bin Data
# Often times you have numerical data on very large scales.
# Sometimes,it can be easier to bin the values into groups.
# This is helpful to more easily perform descriptive statistics by groups as a generalization of patterns in the data.

# Binning in Pandas with Age Example
# Create Random Age Data
# First, let's create a simple pandas DataFrame assigned to the variable df_ages with just one column for age.
# This column will contain 8 random age values between 21 inclusive and 51 exclusive,

df_ages = pd.DataFrame({'age': np.random.randint(21, 51, 8)})

# Print out df_ages.
print(df_ages)

# Create New Column of age_bins Via Defining Bin Edges
# This code creates a new column called age_bins that sets the x argument to the age column in df_ages
# and sets the bins argument to a list of bin edge values.
# The left bin edge will be exclusive and the right bin edge will be inclusive.
# The bins will be for ages: (20, 29] (someone in their 20s), (30, 39], and (40, 49].

# df_ages['age_bins'] = pd.cut(x=df_ages['age'], bins=[20, 29, 39, 49])
df_ages['age_bins'] = pd.cut(x=df_ages['age'], bins=30)

# Print out df_ages.
# We can see age values are assigned to a proper bin.
print(df_ages)

# Let's verify the unique age_bins values.

df_1 = pd.DataFrame(df_ages['age_bins'])
print(df_1)
print(df_ages['age_bins'].unique())

# df[['col1', 'col2', 'col3', 'col4']].groupby(['col1', 'col2']).agg(['mean', 'count'])
print(df_ages[['age', 'age_bins']].groupby(['age_bins']).agg(['mean', 'count']))


# result = df['col1','col2','col3','col4'].groupby(['col1', 'col2']).mean()
# counts = times.groupby(['col1', 'col2']).size()
# result['count'] = counts

# Create New Column of of age_by_decade With Labels 20s, 30s, and 40s
# This code creates a new column called age_by_decade with the same first 2 arguments as above,
# and a third argument of labels set to a list of values that correspond
# to how the age values will be put in bins by decades.

df_ages['age_by_decade'] = pd.cut(x=df_ages['age'], bins=[20, 29, 39, 49], labels=['20s', '30s', '40s'])

# Print out df_ages.
print(df_ages)

# raise ValueError('Bin labels must be one fewer than '
# ValueError: Bin labels must be one fewer than the number of bin edges
