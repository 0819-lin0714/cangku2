# 1．导入Sklearn自带的鸢尾花数据集
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
# 2．拆分数据集
x,y=load_iris().data[:,2:4],load_iris().target   
x_train,x_test,y_train,y_test=train_test_split(x,y, random_state=0,test_size=50)
# 3．训练模型
model=RandomForestClassifier(n_estimators=10,random_state=0)
model.fit(x_train,y_train)
# 4．评估模型
pred=model.predict(x_test)
ac=accuracy_score(y_test,pred)
print("随机森林模型的预测准确率：",ac)