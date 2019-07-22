# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.density.html
import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')
import seaborn as sns
sns.set()

# Create some data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)

# Plot the data with Matplotlib defaults
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

# Histograms, KDE, and densities
# Often in statistical data visualization, all you want is to plot histograms and
# joint distributions of variables. We have seen that this is relatively straightforward in Matplotlib:

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    plt.hist(data[col], density=True, alpha=0.5)

plt.show()

# Rather than a histogram, we can get a smooth estimate of the distribution using a kernel density estimation,
# which Seaborn does with sns.kdeplot:

for col in 'xy':
    sns.kdeplot(data[col], shade=True)

plt.show()

# Histograms and KDE can be combined using distplot:

sns.distplot(data['x'])
sns.distplot(data['y'])

plt.show()