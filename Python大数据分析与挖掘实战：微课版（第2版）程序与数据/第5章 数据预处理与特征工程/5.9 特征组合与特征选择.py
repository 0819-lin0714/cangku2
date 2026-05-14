import numpy as np
data=np.load('data.npy')
data=data[:,1:]

from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(data)
data=imp.transform(data)

from sklearn.preprocessing import StandardScaler
X=data
scaler = StandardScaler()
scaler.fit(X)
X=scaler.transform(X)


from sklearn.preprocessing import MinMaxScaler   
X1=data
min_max_scaler = MinMaxScaler()
min_max_scaler.fit(X1)
x1=min_max_scaler.transform(X1)



