import pandas as pd
data = pd.read_excel('credit.xlsx')
x = data.iloc[:600,:14]
y = data.iloc[:600,14]
x1= data.iloc[600:,:14]
y1= data.iloc[600:,14]
from sklearn.linear_model import LogisticRegression as LR
lr = LR()   #创建逻辑回归模型类
lr.fit(x, y) #训练数据
r=lr.score(x, y); # 模型准确率（针对训练数据）
R=lr.predict(x1)
Z=R-y1
Rs=len(Z[Z==0])/len(Z)
print('预测结果为：',R)
print('预测准确率为：',Rs)


