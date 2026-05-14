import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import LinearRegression as LR
#构造三个变量且不含缺失值的原始数据集x_raw，变量之间满足x3=x1+2*x2
x_raw=[[1,2,5], [3, 6,15],[4,8,20],[1,3,7],[7,2,11],
         [2,4,10],[5,4,13], [2,3,8], [3,3,9],[4,5,14]]
#对x_raw数据集，产生部分缺失值，记为x_miss
x_miss=[[1,2,5], [3, 6,15], [4,8,20], [1,np.nan,7], [7,2,np.nan],
          [2,4,10],[np.nan,4,13],[2,3,8],[3,np.nan,9],[4,5,14]]
x_raw=np.array(x_raw)
x_miss=np.array(x_miss)
imp = IterativeImputer(estimator=LR(),max_iter=15, random_state=0)
imp.fit(x_miss)
#对x_miss填充后的数据集，记为x_imp
x_imp=imp.transform(x_miss)

