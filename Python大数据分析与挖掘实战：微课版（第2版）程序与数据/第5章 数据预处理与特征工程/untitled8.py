from sklearn.datasets import load_iris #加载莺尾花数据集
from sklearn.feature_selection import chi2  #卡方检验
import numpy as np
data2=load_iris() #莺尾花数据集信息
X=data2.data   #莺尾花数据集特征变量
y = data2.target #莺尾花数据集目标分类变量
chi2_value,p_value=chi2(X,y) #获得统计量值和检验p值
p_value=np.round(p_value,4)
