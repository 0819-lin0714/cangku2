import pandas as pd
data = pd.read_excel('发电场数据.xlsx')
x = data.iloc[:,0:4]
y = data.iloc[:,4]
from sklearn.neural_network import MLPRegressor
clf = MLPRegressor(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=8, random_state=1) 
clf.fit(x, y);   
rv=clf.score(x,y)
import numpy as np
x1=np.array([28.4,50.6,1011.9,80.54])
x1=x1.reshape(1,4)
R=clf.predict(x1)   
print('样本预测值为：',R)

