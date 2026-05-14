# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 00:48:45 2020

@author: Lukas
"""

# 加载画图、tensroflow等必要模块
import matplotlib.pyplot as plt  #画图模块
import pandas as pd   #数据读取、处理模块
import seaborn as sns #数据可视化、画各类图形,cmd 中activate tensorflow 后pip install seaborn安装
import tensorflow as tf


#下载数据
dataset_path = tf.keras.utils.get_file("auto-mpg.data", "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
print(dataset_path)   # 注意下载数据之后的地址

#使用 pandas 导入数据集。
column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight',
                'Acceleration', 'Model Year', 'Origin']       #选定需要的数据属性
raw_dataset = pd.read_csv(dataset_path, names=column_names,
                      na_values = "?", comment='\t',
                      sep=" ", skipinitialspace=True)    #读取刚下载的数据

dataset = raw_dataset.copy()#复制数据集
dataset.shape
dataset.tail()   #查看最后5行数据


#数据清洗,数据集中包括一些缺漏、空值等异常值。

dataset.isna().sum()

#为了保证数据值简单可用，删除这些异常值的行。

dataset = dataset.dropna()
print(dataset.shape)
print(dataset.head())

#"Origin" 列实际上代表分类，而不仅仅是一个数字。所以把它转换为独热码 （one-hot）:

origin = dataset.pop('Origin')  #把这列取出，pop()函数移除列表中元素并赋值

dataset['USA'] = (origin == 1)*1.0      #添加USA这一列，当orgin为1的时候赋值1
dataset['Europe'] = (origin == 2)*1.0
dataset['Japan'] = (origin == 3)*1.0
dataset.tail() #倒数最后5派数据



#拆分训练数据集和测试数据集,将数据集拆分为一个训练数据集和一个测试数据集。
train_dataset = dataset.sample(frac=0.8,random_state=0)
test_dataset = dataset.drop(train_dataset.index)  
print(train_dataset.shape)
#print(train_dataset.head())



#也可以查看总体的数据统计:
train_stats = train_dataset.describe()
train_stats.pop("MPG")
train_stats = train_stats.transpose()
print(train_stats)

#数据检查\快速查看训练集中几对列的联合分布。

sns.pairplot(train_dataset[["MPG", "Cylinders", "Displacement", "Weight"]], diag_kind="kde")


#从标签中分离特征\将特征值从目标值或者"标签"中分离。 这个标签是你使用训练模型进行预测的值。

train_labels = train_dataset.pop('MPG')#训练集去掉MPG值
test_labels = test_dataset.pop('MPG')

#数据标准化

def norm(x):
  return (x - train_stats['mean']) / train_stats['std'] #标准化公式

normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)


#构建模型

#建立3层网络，结点[64,64,1]，激活函数用的是relu函数
def build_model():
  model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
  ])
#自定义RMSprop优化器，学习率是0.001
  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mse',   #损失用mse
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model


#模型实例化
model = build_model()

#检查模型,使用 .summary 方法来打印该模型的简单描述。

model.summary()



#训练模型\
#对模型进行100个循环的训练，并在 history 对象中记录训练和验证的准确性。
history = model.fit(
  normed_train_data, train_labels,
  epochs=100, validation_split = 0.2, verbose=0)  #verbose=0表示不输出训练记录


#输出训练的各项指标值
hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()


#把训练结果用图形表示出来
def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch

  plt.figure()
  plt.xlabel('训练次数')
  plt.ylabel('平均绝对误差 [MPG]')
  plt.plot(hist['epoch'], hist['mae'],
           label='训练误差')
  plt.plot(hist['epoch'], hist['val_mae'],
           label = '测试集误差')
  plt.ylim([0,5])
  plt.legend()

  plt.figure()
  plt.xlabel('训练次数')
  plt.ylabel('均方误差[$MPG^2$]')
  plt.plot(hist['epoch'], hist['mse'],
           label='训练误差')
  plt.plot(hist['epoch'], hist['val_mse'],
           label = '测试集误差')
  plt.ylim([0,20])
  plt.legend()
  plt.show()


plot_history(history)   #把平均绝对误差 与均方误差的图画出来



#用测试集来看看泛化模型的效果如何。

loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=2)

print("测试集的平均绝对误差是: {:5.2f} MPG".format(mae))
 

#预测，使用测试集中的数据预测 MPG 值:

test_predictions = model.predict(normed_test_data).flatten()
# 画图表示
plt.scatter(test_labels, test_predictions)
plt.xlabel('真实值 [MPG]')
plt.ylabel('预测值 [MPG]')
plt.axis('equal')
plt.axis('square')
plt.xlim([0,plt.xlim()[1]])
plt.ylim([0,plt.ylim()[1]])
plt.plot([-100, 100], [-100, 100])



