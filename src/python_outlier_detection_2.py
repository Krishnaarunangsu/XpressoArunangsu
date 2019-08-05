import pandas as pd
import numpy as np


def get_outliers(df):
    """

    :param data:
    :return:
    """
    print(f'Age:\n{df.Age}')
    print(f'Mean:{df.Age.mean()}')
    print(f'Age Difference with Mean Age:\n{np.abs(df.Age-df.Age.mean())}')
    print(f'Age Standard Deviation:{df.Age.std()}')
    value_inclusive = df[np.abs(df.Age-df.Age.mean()) <= (df.Age.std())]
    print(f'Value Inclusive:\n{value_inclusive}')

if __name__=="__main__":
    df = pd.read_csv('../data/PersonalData.csv')
    print(df)
    get_outliers(df)
