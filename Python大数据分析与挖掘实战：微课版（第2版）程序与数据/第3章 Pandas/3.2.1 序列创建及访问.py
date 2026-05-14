# -*- coding: utf-8 -*-
import pandas as pd       #导入Pandas库
import numpy as np       #导入Numpy库
s1=pd.Series([1,-2,2.3,'hq'])  #指定列表创建默认序列
s2=pd.Series([1,-2,2.3,'hq'],index=['a','b','c','d'])  #指定列表和索引，创建个性化序列
s3=pd.Series((1,2,3,4,'hq'))                  #指定元组创建默认序列
s4=pd.Series(np.array([1,2,4,7.1]))            #指定数组创建默认序列
#通过字典创建序列
mydict={'red':2000,'bule':1000,'yellow':500}    #定义字典
ss=pd.Series(mydict)                       #指定字典创建序列

print(s1[3])
print(s2['c'])

