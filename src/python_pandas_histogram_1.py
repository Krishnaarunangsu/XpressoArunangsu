import pandas as pd
import numpy as np

df4 = pd.DataFrame({'a': np.random.randn(1000) + 1})
print(f'Hi:\n{df4["a"].hist()}')


count,division = np.histogram(df4['a'])
print(f':\n{count}')
print(f':\n{division}')
print('**************************************************')
print(f'HIIII:\n{pd.cut(df4["a"], 10).value_counts()}')
