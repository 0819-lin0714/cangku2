# -*- coding: utf-8 -*-
import pandas as pd
s5=[1,2,2,3,'hq','hq','he']      #定义列表s5
s5=pd.Series(s5)            #将定义的列表s5转换为序列
s51=s5.unique()            #调用unique()方法去重
print(s51)                 #打印结果

s52=s5.isin([0,'he'])
print(s52)

s53=s5.value_counts()

import numpy as np
ss1=pd.Series([10,'hq',60,np.nan,20])  #定义序列ss1，其中np.nan为空值（nan值）
tt1=ss1[~ss1.isnull()]     #~为取反，采用逻辑数组进行索引获取数据

tt2=ss1[ss1.notnull()]   
tt3=ss1.dropna()
