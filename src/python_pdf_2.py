# https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.stats.norm.html
# Normal Distribution

import scipy.stats
import numpy as np
import matplotlib.pyplot as plt

# Set the seed
from numpy.core._multiarray_umath import ndarray

np.random.seed(1234)

# Get the samples
samples = np.random.lognormal(mean=1., sigma=.4, size=10000)

# Get shape, loc = mean, scale = standard deviation
shape, loc, scale = scipy.stats.lognorm.fit(samples, floc=0)

# bins for bucketing
num_bins = 50

# Graph building
clr = "#EFEFEF"
counts, edges, patches = plt.hist(samples,bins=num_bins, color=clr)
centers = 0.5*(edges[:-1]+edges[1:])
cdf = scipy.stats.lognorm.cdf(edges, shape, loc=loc, scale=scale)
print(cdf)
print('*****************************************************************')
prob: ndarray = np.diff(cdf)
print(prob)
plt.plot(centers, samples.size*prob, 'k-', linewidth=2)
plt.show()

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.diff.html
# https://www.w3cschool.cn/doc_numpy_1_11/numpy_1_11-generated-numpy-diff.html
# https://blog.finxter.com/numpy-np-diff-simply-explained-bonus-video/
# https://www.programcreek.com/python/example/21342/numpy.diff