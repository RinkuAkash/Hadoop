import pandas as pd
import numpy as np

user_log = pd.read_csv("CpuLogData2019-10-24.csv")

filtered_columns = []

for column in user_log.columns:
    column = column.strip()
    column = column.replace(" ", "_")
    column = column.replace("/", "")
    filtered_columns.append(column)

user_log.columns = filtered_columns
indices = []

for index in user_log.index:
    if '2019-10-25' in user_log['DateTime'].iloc[index]:
        indices.append(index)
user_log.replace(user_log.isnull(), 0, inplace=True)
user_log.fillna(np.nan, inplace=True)
user_log.drop(user_log.index[indices], inplace=True)
user_log.to_csv("userlog_filtered_data.csv", index=False)
