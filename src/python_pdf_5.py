# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# https://rstudio-pubs-static.s3.amazonaws.com/365322_017ceefa9b624b2291ef1ccfb8451ce1.html
# https://github.com/MayukhSobo/Loan_EDA
# https://codefellows.github.io/sea-python-401d2/lectures/stats_day2.html
# https://kite.com/blog/python/data-analysis-visualization-python

data = pd.read_csv("../data/prosperLoanData.csv", sep=",")
data = data[data.StatedMonthlyIncome < 2E4]
H, edges = np.histogram(data.StatedMonthlyIncome, bins=2)

print(f'H:\n{H}')
print(f'Edges:\n{edges}')

plt.figure(figsize=(10, 4))
ax = plt.subplot(111)
ax.bar(edges[:-1], H / float(sum(H)), width=edges[1] - edges[0])
ax.text(0.9, 0.9, "%g loans" % len(data),
        horizontalalignment="right", transform=ax.transAxes)
ax.set_xlabel("Stated Monthly Income ($)")
ax.set_ylabel("Probability of Income Range")
ax.minorticks_on()
plt.show()

H, edges = np.histogram(data.StatedMonthlyIncome, bins=4)
print(f'H:\n{H}')
print(f'Edges:\n{edges}')

plt.figure(figsize=(10, 4))
ax = plt.subplot(111)
ax.bar(edges[:-1], H / float(sum(H)), width=edges[1] - edges[0])
ax.text(0.9, 0.9, "%g loans" % len(data),
        horizontalalignment="right", transform=ax.transAxes)
ax.set_xlabel("Stated Monthly Income ($)")
ax.set_ylabel("Probability of Income Range")
ax.minorticks_on()
plt.show()

H, edges = np.histogram(data.StatedMonthlyIncome, bins=20)
print(f'H:\n{H}')
print(f'Edges:\n{edges}')

plt.figure(figsize=(10, 4))
ax = plt.subplot(111)
ax.bar(edges[:-1], H / float(sum(H)), width=edges[1] - edges[0])
ax.text(0.9, 0.9, "%g loans" % len(data),
        horizontalalignment="right", transform=ax.transAxes)
ax.set_xlabel("Stated Monthly Income ($)")
ax.set_ylabel("Probability of Income Range")
ax.minorticks_on()
plt.show()
