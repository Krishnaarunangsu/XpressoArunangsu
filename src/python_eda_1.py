# Objective
# To classify/predict a patient survival who had undergone surgery for breast cancer.


import pandas as pd # Data analysis and manipulation
import numpy as np # Numerical operations

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns
# To load the data into DataFrame(It is 2d mutable, heterogeneous tabular data structure with labeled axes)

#df = pd.read_csv("haberman.csv")
from pandas import DataFrame

df = pd.read_csv('../data/haberman.csv')
print(df.head())
print(df.columns)
print(df.shape)



# To rename the column name for better understanding
# Both of the ways we can rename the columns name

#df.columns = ["age", "operation_year", "axillary_lymph_node", "survival_status"]

#or

df: DataFrame = df.rename(columns={"30": "age", "64": "operation_year", "1": "axillary_lymph_node", "1.1": "survival_status"})
# It gives you the top 5 rows(data-points).

df.head()
# To look at the last 5 rows(data-points), we can also specify that how many data-points we want to see.

df.tail(7)

# To know about data summary

df.info()
# To know statistical summary of data which is very important

df.describe()

# To know number of data-points for each class.
# As it is not balanced dataset, it is imbalanced dataset because the number of data-points for both of the class are significantly different.
# we will see how to handle imbalanced data later

df.survival_status.value_counts()

# Univariate Analysis(pdf, cdf, boxplot and violin plot) Univariate analysis is the simplest form of analyzing data.
# “Uni” means “one”, "variate" means "variable or numeric variable" so, in other words your data has only one
# variable. It doesn't deal with causes or relationships (unlike regression) and it's major purpose is to describe;
# it takes data, summarizes that data and finds patterns in the data.

# PDF(Probability Density Function)
# # Here, we are using age feature to generate pdf()
# # pdf(smoothed form of histogram)
# # pdf basically shows, how many of points lies in some interval
#
sns.FacetGrid(df, hue="survival_status", height=5).map(sns.distplot, "age").add_legend()
plt.title("Histogram of age")
plt.ylabel("Density")
plt.show()


sns.FacetGrid(df, hue = "survival_status", height=5). map(sns.distplot, "operation_year").add_legend()
plt.title("Histogram of operation_year")
plt.ylabel("Density")
plt.show()


sns.FacetGrid(df, hue = "survival_status", height=5).map(sns.distplot, "axillary_lymph_node").add_legend()
plt.title("Histogram of axillary_lymph_node")
plt.ylabel("Density")
plt.show()

# CDF(Cummulative Distributed Function)
# one = df.loc[df["survival_status"] == 1]
# two = df.loc[df["survival_status"] == 2]
# cdf gives you cummulative probability associated with a function
# Cumulative sum of area under curve upto gives you cdf
# Here, Class 1 means survived
# Class 2 means not survived
one = df.loc[df["survival_status"] == 1]
two = df.loc[df["survival_status"] == 2]
label = ["pdf of class 1", "cdf of class 1", "pdf of class 2", "cdf of class 2"]
counts, bin_edges = np.histogram(one["age"], bins=10, density=True)
pdf = counts/(sum(counts))
cdf = np.cumsum(pdf)
plt.title("pdf and cdf for age")
plt.xlabel("age")
plt.ylabel("% of person's")
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)

counts, bin_edges = np.histogram(two["age"], bins=10, density=True)
pdf = counts/(sum(counts))
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)
plt.legend(label)
plt.show()



label = ["pdf of class 1", "cdf of class 1", "pdf of class 2", "cdf of class 2"]
counts, bin_edges = np.histogram(one["operation_year"], bins=10, density = True)
pdf = counts/(sum(counts))
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)


counts, bin_edges = np.histogram(two["operation_year"], bins=10, density=True)
pdf = counts/(sum(counts))
cdf = np.cumsum(pdf)
plt.title("pdf and cdf for operation_year")
plt.xlabel("operation_year")
plt.ylabel("% of person's")
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)
plt.legend(label)
plt.show()


label = ["pdf of class 1", "cdf of class 1", "pdf of class 2", "cdf of class 2"]
counts, bin_edges = np.histogram(one["axillary_lymph_node"], bins=10, density = True)
pdf = counts/(sum(counts))
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)

counts, bin_edges = np.histogram(two["axillary_lymph_node"], bins=10, density = True)
pdf = counts/(sum(counts))
cdf = np.cumsum(pdf)
plt.title("pdf and cdf for axillary_lymph_node")
plt.xlabel("axillary_lymph_node")
plt.ylabel("% of person's")
plt.plot(bin_edges[1:], pdf)
plt.plot(bin_edges[1:], cdf)
plt.show()


# Box Plot
# boxplot gives you the statistical summery of data
# Rectangle represent the 2nd and 3rd quartile (horizontal line either side of the rectangle)
# The horizontal line inside box represents median
# We can add title in box plot using either way
# plt.title("Box plot for survival_status and age") or set_title("")
sns.boxplot(x="survival_status", y="age", hue="survival_status", data=df)\
    .set_title("Box plot for survival_status and age")
plt.show()


sns.boxplot(x="survival_status", y="operation_year", hue="survival_status", data=df)\
    .set_title("Box plot for survival_status and operation_year")
plt.show()

sns.boxplot(x="survival_status", y="axillary_lymph_node", hue = "survival_status", data=df)\
    .set_title("Box plot for survival_status and axillary_lymph_node")
plt.show()

# Violin Plot
# # The violin plot shows the full distribution of the data.
# # It is combination of box plot and histogram
# # central dot represents median
#
sns.violinplot(x = "survival_status", y = "age", hue = "survival_status", data = df)
plt.title("Violin plot for survival_status and age")
plt.show()


sns.violinplot(x = "survival_status", y = "operation_year", hue = "survival_status", data = df)
plt.title("Violin plot for survival_status and operation_year")
plt.show()

sns.violinplot(x = "survival_status", y = "axillary_lymph_node", hue = "survival_status", data = df)
plt.title("Violin plot for survival_status and axillary_lymph_node")
plt.show()


# Bivariate Analysis
# https://www.kaggle.com/premvardhan/exploratory-data-analysis-haberman-s-survival/data


