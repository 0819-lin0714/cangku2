from imblearn.over_sampling import SMOTE  
import pandas as pd
raw_data = pd.read_excel('D.xlsx')
model_smote = SMOTE()  
X,y = raw_data.iloc[:, :-1],raw_data.iloc[:, -1]  # 分割X,y
X_s, y_s = model_smote.fit_resample(X,y)  
print('原始数据0类样本数：',len(y[y==0]))
print('原始数据1类样本数：',len(y[y==1]))
print('抽样数据0类样本数：',len(y_s[y_s==0]))
print('抽样数据1类样本数：',len(y_s[y_s==1]))