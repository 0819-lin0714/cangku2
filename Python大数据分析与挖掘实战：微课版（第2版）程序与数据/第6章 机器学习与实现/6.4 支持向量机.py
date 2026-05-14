import pandas as pd
data = pd.read_excel('car.xlsx')
x = data.iloc[:1690,:6].values
y = data.iloc[:1690,6].values
x1= data.iloc[1691:,:6].values
y1= data.iloc[1691:,6].values
from sklearn import svm
clf = svm.SVC(kernel='rbf')  
clf.fit(x, y) 
rv=clf.score(x, y);
R=clf.predict(x1)
Z=R-y1
Rs=len(Z[Z==0])/len(Z)
print('预测结果为：',R)
print('预测准确率为：',Rs)

