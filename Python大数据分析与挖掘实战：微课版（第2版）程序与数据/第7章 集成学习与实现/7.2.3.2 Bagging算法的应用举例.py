from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

x,y=load_iris().data,load_iris().target   
x_train,x_test,y_train,y_test=train_test_split(x,y,
random_state=0,test_size=0.5)

k_range=range(1,15)		       #设置k值的取值范围
k_error=[]	                      #k_error用于保存预测误差率数据
for k in k_range:
    model=KNeighborsClassifier(n_neighbors=k)
    scores=cross_val_score(model,x,y,cv=5,scoring='accuracy')
    k_error.append(1-scores.mean())
# 1．定义模型
kNNmodel=KNeighborsClassifier(6)        #k近邻模型
Baggingmodel=BaggingClassifier(KNeighborsClassifier(6),
n_estimators=130,max_samples=0.4,max_features=4,random_state=1)
					                      #Bagging模型
# 2．训练模型
kNNmodel.fit(x_train,y_train)
Baggingmodel.fit(x_train,y_train)
# 3．评估模型
kNN_pre=kNNmodel.predict(x_test)
kNN_ac=accuracy_score(y_test,kNN_pre)
print("k近邻模型预测准确率：",kNN_ac)
Bagging_pre=Baggingmodel.predict(x_test)
Bagging_ac=accuracy_score(y_test,Bagging_pre)
print("基于k近邻算法的Bagging模型的预测准确率：",Bagging_ac)