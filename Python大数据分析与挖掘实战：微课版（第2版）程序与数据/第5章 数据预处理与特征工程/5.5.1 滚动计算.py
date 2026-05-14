import pandas as pd
list_data=[10,4,3,8,15,26,17,80,12,5]
series_data=pd.Series(list_data)
rolling_sum=series_data.rolling(5).sum()
rolling_mean=series_data.rolling(5).mean()
rolling_max=series_data.rolling(5).max()
rolling_min=series_data.rolling(5).min()
rolling_median=series_data.rolling(5).median()
rolling_var=series_data.rolling(5).var()
rolling_std=series_data.rolling(5).std()

