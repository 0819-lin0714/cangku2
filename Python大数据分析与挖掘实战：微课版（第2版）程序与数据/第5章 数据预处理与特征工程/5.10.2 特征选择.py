#1．方差阈值选择法
from sklearn.feature_selection import VarianceThreshold #方差阈值选择模块
import pandas as pd
import numpy as np

X = np.load('boston_data.npy')

X_var = pd.DataFrame(X).var()             #计算各自变量方差
select1 = VarianceThreshold(threshold=3)#构建特征选择对象，方差阈值设置为3
X_select1= select1.fit_transform(X)      #对于X训练并转换
X_shape=X.shape                              #原始数据集规模尺寸
X_select1_shape=X_select1.shape           #特征选择后的数据集规模尺寸

#2．Pearson相关系数法
from scipy import stats
res2=[]  #存放计算结果（相关系数，p值）
y = np.load('boston_target.npy') #提取目标变量
for i in range(X.shape[1]):
    X_pear = stats.pearsonr(X[:, i], y)   #Pearson相关系数方法
    res2.append((X_pear[0],round(X_pear[1],4))) #p值保留4位小数
    

#3. 曼惠特尼U检验法
from scipy.stats import mannwhitneyu    #曼惠特尼U检验
res3=[]  #存放计算结果（统计量，p值）
for i in range(X.shape[1]):
    stat, p=mannwhitneyu(X[:, i], y)
    res3.append((stat,round(p,4)))

#4. 卡方检验法
from sklearn.datasets import load_iris #加载莺尾花数据集
from sklearn.feature_selection import chi2  #卡方检验
import numpy as np
data2=load_iris() #莺尾花数据集信息
X=data2.data   #莺尾花数据集特征变量
y = data2.target #莺尾花数据集目标分类变量
chi2_value,p_value=chi2(X,y) #获得统计量值和检验p值
p_value=np.round(p_value,4)

from sklearn.feature_selection import SelectKBest
x_select4 = SelectKBest(chi2, k=3).fit_transform(X, y)#chi2为前面导入的卡方检验

#5. 特征重要度法
from sklearn.linear_model import LinearRegression as LR
from sklearn.ensemble import GradientBoostingRegressor as gbr
X = np.load('boston_data.npy')
y = np.load('boston_target.npy') #提取目标变量
model_1=LR()             #线性回归模型对象
model_1.fit(X,y)         
r1=model_1.score(X,y)   	
coef_x=model_1.coef_      #线性回归模型变量系数
model_2=gbr()          #梯度增强回归模型对象
model_2.fit(X,y)
r2=model_2.score(X,y)   	
importances_x=model_2.feature_importances_  #特征重要度

from sklearn.inspection import permutation_importance
result_1 = permutation_importance(model_1, X,y, n_repeats=10,random_state=0)
result_2 = permutation_importance(model_2, X,y, n_repeats=10,random_state=0)
importances1_x=result_1.importances_mean
importances2_x=result_2.importances_mean

#6. 递归特征消除法（RFE）
from sklearn.feature_selection import RFE           #导入递归特征消除法模块
rfe = RFE(estimator=gbr(), n_features_to_select=6,step=1)#指定最优特征个数K=6
rfe.fit(X,y)
x_select6=rfe.transform(X)
x_support=rfe.support_

from sklearn.model_selection import cross_val_score #交叉检验模块
import matplotlib.pyplot as plt
re = []
for i in range(1,14):
    rfe = RFE(estimator=gbr(),n_features_to_select=i, step=1)
    rfe.fit(X, y)
    x_select6= rfe.transform(X)
    r = cross_val_score(gbr(), x_select6, y, cv=5).mean()
    re.append(r)
plt.plot(range(1,14),re,'r*-')
plt.show()