# -*- coding: utf-8 -*-
import pandas as pd       
import numpy as np       
s1=pd.Series([1,-2,2.3,'hq'])
s2=pd.Series([1,-2,2.3,'hq'],index=['a','b','c','d'])  
s4=pd.Series(np.array([1,2,4,7.1]))
s22=s2[['a','d']]        #取索引号为字符a,b的元素
s11=s1[0:2]           #索引为连续的数组
s12=s1[[0,2,3]]        #索引为不连续的数组
s41=s4[s4>2]         #索引为逻辑数组
print(s22)
print('-'*20)
print(s11)
print('-'*20)
print(s12)
print('-'*20)
print(s41)


