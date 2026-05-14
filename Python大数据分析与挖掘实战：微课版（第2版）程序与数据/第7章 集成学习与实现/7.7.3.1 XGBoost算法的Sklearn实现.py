# 1．加载数据集，并划分训练集和测试集
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
#  2．调整参数
filename="./glass.data"
glass_data = pd.read_csv(filename,index_col=0,header=None)
X,y = glass_data.iloc[:,:-1].values, glass_data.iloc[:,-1].values
#XGBClassifier中初始化参数use_label_encoder已被弃用
#新的程序建议设置use_label_encoder=False，此时，
#  类别标签必须为整数，值从0开始到类别总数-1，并且是连续的值
y=y-1   			# 原来类别编码从1开始，所以要减去1
#原始类别编号没有4，因此y=y-1后没有3，新编号4至6的要再减去1
y[y==4]=3
y[y==5]=4
y[y==6]=5
#print(y)
#  3．用XGBClassifier创建并训练梯度提升分类器模型
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, stratify=y, random_state=0)
# 用XGBClassifier创建并训练梯度提升分类器模型
# 从XGBoost 1.3.0开始，与目标函数objective='multi:softprob'一起使用的默认评估指标从
# 'merror'更改为'mlogloss'。如果想恢复为'merror'，显式地设置eval_metric="merror"。
xgbc=XGBClassifier(n_estimators=500,use_label_encoder=False,objective='multi:softprob',eval_metric="merror")
xgbc.fit(X_train, y_train)
print("训练集准确率：", xgbc.score(X_train, y_train), sep="")
print("测试集准确率：", xgbc.score(X_test, y_test), sep="") 
print("对测试集前2个样本预测的分类标签：\n",xgbc.predict(X_test[:2]), sep="")
print("对测试集前2个样本预测的分类概率：\n",
      xgbc.predict_proba(X_test[:2]), sep="") 
print("分类器中的标签排列：",xgbc.classes_)
# 概率预测转化为标签预测
print("根据预测概率推算预测标签：",end="")
for i in xgbc.predict_proba(X_test[:2]).argmax(axis=1):
    print(xgbc.classes_[i], end="  ")
print("\n测试集前2个样本的真实标签：",y_test[:2],sep="")