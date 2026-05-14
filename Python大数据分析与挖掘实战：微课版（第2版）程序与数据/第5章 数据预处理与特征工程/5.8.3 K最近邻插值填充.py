import numpy as np
from sklearn.metrics.pairwise import nan_euclidean_distances
x = np.array([1,np.nan,5])
y = np.array([1,3,6])
x=x.reshape(1,-1)
y=y.reshape(1,-1)
temp=[[1,2,5], [3, 6,15], [4,8,20], [1,np.nan,7], [7,2,np.nan]] 
temp=np.array(temp)
#距离计算
d=nan_euclidean_distances(x, y)
temp_d=nan_euclidean_distances(temp, temp)

from sklearn.impute import KNNImputer #导入k最近邻插补模块
imp = KNNImputer(n_neighbors=2)#创建对象，并且k取2
imp.fit(temp)                      #拟合训练
temp_imp=imp.transform(temp)    #返回填补看结果

