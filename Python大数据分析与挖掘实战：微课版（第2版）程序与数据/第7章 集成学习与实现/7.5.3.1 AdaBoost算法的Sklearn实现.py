# 1．导入Sklearn自带的鸢尾花数据集
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier 
# 2．采用AdaBoostClassifier建立分类模型
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit	
# 3．拆分数据集
x,y=load_iris().data,load_iris().target   
x_train,x_test,y_train,y_test=train_test_split(x,y,
random_state=0,test_size=50)
# 4．网格搜索法寻找参数的最优值
param_grid={'n_estimators':[10,20,30,40,50,60,70,80,90,100],'learning_rate':[0.0001,0.0005,0.001,0.005,0.01,0.05,0.1,0.5,0.6,0.7,0.8,0.9]}
cv=StratifiedShuffleSplit(n_splits=5,test_size=0.3,
random_state=420)
grid=GridSearchCV(AdaBoostClassifier(DecisionTreeClassifier(criterion='gini',max_depth=3),random_state=0),param_grid=param_grid,cv=cv)
grid.fit(x_train,y_train)
# 5．获取最优模型
model=grid.best_estimator_					#
pred=model.predict(x_test)
ac=accuracy_score(y_test,pred)
print("最优参数值为：%s"%grid.best_params_)
print("最优参数值对应模型的预测准确率为：%f"%ac)