import pandas as pd
import numpy as np

data_frame = pd.read_csv("TitanicData.txt")
data_frame.columns = ['id', 'survived', 'pclass', 'name', 'sex', 'age', 'sibsp', 'parch', 'ticket', 'fare', 'cabin', 'embarked', 'empty']
data_frame['age'].replace(to_replace='', value=np.nan, inplace=True)
mean_value = data_frame['age'].median()
data_frame['age'].fillna(mean_value, inplace=True)
data_frame.to_csv(r'Titanic_filtered_data.txt', header=None, index=None, sep=',', mode='a')
