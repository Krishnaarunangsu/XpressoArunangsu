# example dataset of normally distributed data.
df = pd.DataFrame({'Data':np.random.normal(size=200)})
print(f'Dataframe:\n{df}')
print('******************************************************')

# keep only the ones that are within +3 to -3 standard deviations in the column 'Data'.
value_inclusive = df[np.abs(df.Data-df.Data.mean()) <= (3*df.Data.std())]
print(f'Value Inclusive:\n{value_inclusive}')

# or if you prefer the other way around
value_inclusive_advanced = df[~(np.abs(df.Data-df.Data.mean()) > (3*df.Data.std()))]
print(f'Value Inclusive:\n{value_inclusive_advanced}')
