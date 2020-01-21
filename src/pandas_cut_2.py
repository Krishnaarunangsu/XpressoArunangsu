import pandas as pd
import numpy as np


def discretize(data, bins=5, quantile=False):
    '''
    Creates 'bins' number of bins and discretizes the data.
    Uses cut function by default. qcut function otherwise.
    '''
    if quantile:
        new_data = pd.qcut(data, bins, labels=list(range(bins)))
    else:
        new_data = pd.cut(data, bins, labels=list(range(bins)))
    return new_data


def transform(self, x):
        """
        Parameters:

            x (Sequence): - ???????

        Returns:

            np.array: - ????????????numpy??

        """
        s = pd.cut(x, bins=self.bins)
        d = pd.get_dummies(s)
        z = d.T.to_dict()
        re = []
        for i, v in z.items():
            for j, u in v.items():
                if u == 1:
                    re.append(str(j))
        return np.array(re)

# https://www.programcreek.com/python/example/101361/pandas.cut