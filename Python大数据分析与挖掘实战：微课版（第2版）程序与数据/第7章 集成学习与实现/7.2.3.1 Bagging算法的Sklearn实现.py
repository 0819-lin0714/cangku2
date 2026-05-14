# 1．定义模型
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
#2．拆分花数据集
x,y=load_iris().data,load_iris().target   
x_train,x_test,y_train,y_test=train_test_split(x,y,
random_state=0,test_size=0.5)
# 3．寻找k近邻模型的最优k值
k_range=range(1,15)		       #设置k值的取值范围
k_error=[]	                      #k_error用于保存预测误差率数据
for k in k_range:
    model=KNeighborsClassifier(n_neighbors=k)
    scores=cross_val_score(model,x,y,cv=5,scoring='accuracy')
    k_error.append(1-scores.mean())
# 4．画图，计算模型的预测误差率（x轴表示k的取值，y轴表示预测误差率）
plt.rcParams['font.sans-serif']='Simhei'
plt.plot(k_range,k_error,'r-')
plt.xlabel('k的取值')
plt.ylabel('预测误差率')
plt.show()