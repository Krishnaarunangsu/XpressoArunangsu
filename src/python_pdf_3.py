# https://data-flair.training/blogs/python-probability-distributions/

import matplotlib.pyplot as plt
import seaborn
from scipy.stats import binom


data = binom.rvs(n=17,p=0.7, loc=0, size=1010)
ax = seaborn.distplot(data,kde=True, color='pink', hist_kws={"linewidth": 22,'alpha':0.77})
ax.set(xlabel='Binomial', ylabel='Frequency')
plt.show()
