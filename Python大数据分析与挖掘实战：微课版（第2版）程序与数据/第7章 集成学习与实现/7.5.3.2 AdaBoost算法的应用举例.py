
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor

# 加载数据集
diabetes = load_diabetes()
X,y = diabetes.data, diabetes.target
# 划分训练集与测试集
X_train, X_test, y_train, y_test = \
    train_test_split(X,y,random_state=0)

# 创建基本回归模型对象
#base_regressor = Ridge(random_state=0)
base_regressor = DecisionTreeRegressor(max_depth=2, random_state=0)
# 创建回归集成器
ada_regressor = AdaBoostRegressor(base_regressor,
                                 n_estimators=1000,
                                 random_state=0)

# 训练模型
for regressor in (base_regressor, ada_regressor):
    regressor.fit(X_train, y_train)
    print(regressor.__class__.__name__,"在训练集决定系数R^2为：",
          regressor.score(X_train, y_train),sep="")
    print(regressor.__class__.__name__,"在测试集决定系数R^2为：",
          regressor.score(X_test, y_test),sep="")
    print(regressor.__class__.__name__,"在测试集前三个样本的预测值：\n",
          regressor.predict(X_test[:3]),sep="")
    
print("测试集前三个样本的真实值：", y_test[:3], sep="")

