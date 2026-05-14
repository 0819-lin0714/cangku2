#1．数据获取
import pandas as pd
data = pd.read_excel('发电场数据.xlsx')
x = data.iloc[:,0:4].values
y = data.iloc[:,4].values
#2．导入线性回归模块（简称LR）
from sklearn.linear_model import LinearRegression as LR
lr = LR()             	#创建线性回归模型类
lr.fit(x, y)         	#拟合
Slr=lr.score(x,y)   	#判定系数R2
c_x=lr.coef_         	#x对应的回归系数
c_b=lr.intercept_   	#回归系数常数项
#3．预测
import numpy as np
x1=np.array([28.4,50.6,1011.9,80.54])
x1=x1.reshape(1,4)
R1=lr.predict(x1)    	#采用自带函数预测
r1=x1*c_x
R2=r1.sum()+c_b      	#计算预测值
print('x回归系数为：',c_x)
print('回归系数常数项为：',c_b)
print('判定系数为：',Slr)
print('样本预测值为：',R1)


