# http://www.learningaboutelectronics.com/Articles/How-to-create-a-probability-density-function-plot-in-Python.php
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import statistics


x = np.arange(-4, 4, 0.001)
print(norm.pdf(x))
plt.plot(x, norm.pdf(x))

mean_from_stat = statistics.mean(x)
print(mean_from_stat)

mean = np.mean(x)
print(mean)
std = np.std(x)
print(norm.cdf(x, mean, std))

plt.show()

# http://www.learningaboutelectronics.com/Articles/How-to-randomly-select-shuffle-list-in-Python.php

