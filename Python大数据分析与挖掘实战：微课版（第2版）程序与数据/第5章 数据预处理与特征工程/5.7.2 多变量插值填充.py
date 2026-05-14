# -*- coding: utf-8 -*-
import pandas as pd
raw_data = pd.read_excel('D.xlsx')
Data_1=raw_data.iloc[raw_data.iloc[:,-1].values==1,:]
Data_0=raw_data.iloc[raw_data.iloc[:,-1].values==0,:]
Data_0=Data_0.sample(n=len(Data_1), replace=True,  random_state=10, axis=0)
simpe_data=pd.concat([Data_1, Data_0], axis = 0)

