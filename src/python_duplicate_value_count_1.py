import pandas as pd
import numpy as np


students = [('jack', 34, 'Sydeny'),
            ('Riti', 30, 'Delhi'),
            ('Aadi', 16, 'New York'),
            ('Riti', 30, 'Delhi'),
            ('Riti', 30, 'Delhi'),
            ('Riti', 30, 'Mumbai'),
            ('Aadi', 40, 'London'),
            ('Sachin', 30, 'Delhi')
            ]

# Create a DataFrame object
dfObj = pd.DataFrame(students, columns=['Name', 'Age', 'City'])
print(dfObj)

duplicateRowsDF = dfObj[dfObj.duplicated()]

print("Duplicate Rows except first occurrence based on all columns are :")
print(duplicateRowsDF)

duplicateRowsDF = dfObj[dfObj.duplicated(['Name'])]

print("Duplicate Rows based on a single column are:", duplicateRowsDF, sep='\n')
