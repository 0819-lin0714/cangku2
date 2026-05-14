# 1．加载数据集，并划分训练集和测试集
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
# 2．创建并训练梯度提升树分类器模型

filename="./glass.data"
glass_data = pd.read_csv(filename,index_col=0,header=None)
X,y = glass_data.iloc[:,:-1].values, glass_data.iloc[:,-1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, stratify=y, random_state=1)
gbc = GradientBoostingClassifier(n_estimators=500)
gbc.fit(X_train, y_train)
print("训练集准确率：", gbc.score(X_train, y_train), sep="")
print("测试集准确率：", gbc.score(X_test, y_test), sep="") 
print("对测试集前2个样本预测的分类标签：\n",gbc.predict(X_test[:2]), sep="")
print("对测试集前2个样本预测的分类概率：\n", gbc.predict_proba(X_test[:2]), sep="") 
print("分类器中的标签排列：",gbc.classes_)
# 概率预测转化为标签预测
print("根据预测概率推算预测标签：",end="")
for i in gbc.predict_proba(X_test[:2]).argmax(axis=1):
    print(gbc.classes_[i], end="  ")
print("\n测试集前2个样本的真实标签：",y_test[:2],sep="")