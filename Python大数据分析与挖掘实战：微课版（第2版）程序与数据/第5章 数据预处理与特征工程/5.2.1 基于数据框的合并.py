# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
dict1={'a':[2,2,'kt',6],'b':[4,6,7,8],'c':[6,5,np.nan,6]}
dict2={'d':[8,9,10,11],'e':['p',16,10,8]}
dict3={'a':[1,2],'b':[2,3],'c':[3,4],'d':[4,5],'e':[5,6]}
df1=pd.DataFrame(dict1)
df2=pd.DataFrame(dict2)
df3=pd.DataFrame(dict3)
del dict1,dict2,dict3
df4=pd.concat([df1,df2],axis=1)#水平合并
df5=pd.concat([df3,df4],axis=0)#垂直合并，有相同的列名，index属性伴随原数据框
df5.index=range(6) #重新设置index属性

