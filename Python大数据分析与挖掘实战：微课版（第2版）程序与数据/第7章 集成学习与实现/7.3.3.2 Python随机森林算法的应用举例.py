# 1．导入Sklearn自带的鸢尾花数据集
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

x,y=load_iris().data[:,2:4],load_iris().target   
x_train,x_test,y_train,y_test=train_test_split(x,y, random_state=0,test_size=50)

model=RandomForestClassifier(n_estimators=10,random_state=0)
model.fit(x_train,y_train)

# 1．绘制3种类别鸢尾花的样本点
x1,x2=np.meshgrid(np.linspace(0,8,500),np.linspace(0,3,500))
x_new=np.stack((x1.flat,x2.flat),axis=1)
y_predict=model.predict(x_new)
y_hat=y_predict.reshape(x1.shape)
iris_cmap=ListedColormap(["#ACC6C0","#FF8080","#A0A0FF"])
plt.pcolormesh(x1,x2,y_hat,cmap=iris_cmap)
plt.scatter(x[y==0,0],x[y==0,1],s=30,c='g',marker='^')
plt.scatter(x[y==1,0],x[y==1,1],s=30,c='r',marker='o')
plt.scatter(x[y==2,0],x[y==2,1],s=30,c='b',marker='s')
# 2．设置坐标轴的名称并显示图形
plt.rcParams['font.sans-serif']='Simhei'
plt.xlabel('花瓣长度')
plt.ylabel('花瓣宽度')
plt.show()