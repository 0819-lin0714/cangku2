import pandas as pd
import numpy as np
data=pd.read_excel('missing.xlsx')                                      #数据框data
c=np.array([[1,2,3,4],[4,5,6,np.nan],[5,6,7,8],[9,4,np.nan,8]])   #数组c
C=pd.DataFrame(c)    

from sklearn.impute import SimpleImputer
fC=C
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(fC)
fC=imp.transform(fC)

imp = SimpleImputer(missing_values=np.nan, strategy='median')
fc=c
imp.fit(fc)
fc=imp.transform(fc)

fD=data[['a','c']]
imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp.fit(fD)
fD=imp.transform(fD)