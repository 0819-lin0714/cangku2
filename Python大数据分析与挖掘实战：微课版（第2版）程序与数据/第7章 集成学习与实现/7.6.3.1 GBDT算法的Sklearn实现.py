# 1．加载加利福尼亚住房数据集，并划分训练集和测试集
#coding=utf-8
#example12_9_GradientBoostingRegressor.py
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
#  2．创建并训练梯度提升回归树模型
housing = fetch_california_housing(data_home="./dataset")
X, y = housing.data, housing.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
gbr = GradientBoostingRegressor(n_estimators=500)
gbr.fit(X_train, y_train)
print("训练集决定系数R^2：",gbr.score(X_train,y_train))
print("测试集决定系数R^2：",gbr.score(X_test,y_test))
print("测试集前3个样本的预测值：",gbr.predict(X_test[:3]))
print("测试集前3个样本的真实值：",y_test[:3])