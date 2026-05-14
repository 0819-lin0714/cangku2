# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:26:06 2020

@author: Lukas
"""



#加载tensorflow框架
import tensorflow as tf

mnist = tf.keras.datasets.mnist  #MNIST数据集加载

(x_train_all, y_train_all),(x_test, y_test) = mnist.load_data()  #将数据集划分成训练集与测试集
 #将Mnist数据集简单归一化
x_train_all, x_test = x_train_all / 255.0, x_test / 255.0

# 对数据集进行划分，50009个为训练集，10000个为验证集
x_train, x_valid = x_train_all[:50000], x_train_all[50000:]  #验证集10000个
y_train, y_valid = y_train_all[:50000], y_train_all[50000:]
print(x_train.shape)
print(y_train.shape)

#打印一张照片
'''
import matplotlib.pyplot as plt   #加载画图模快

def show_single_image(img_arr):    #定义一个提取图像函数
      plt.imshow(img_arr,cmap='binary')   #展示图像
      plt.show()
      
show_single_image(x_train[1])
'''

#将模型的各层堆叠起来，以层的方式搭建 tf.keras.Sequential 模型。
import tensorflow.keras as keras
from tensorflow.keras import models, layers, optimizers #序列模型

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),  #输入层
  tf.keras.layers.Dense(256, activation=tf.nn.relu),  #隐藏层1
  tf.keras.layers.Dropout(0.2),   #百分之20的神经元不工作，防止过拟合
  tf.keras.layers.Dense(128, activation=tf.nn.relu),  #隐藏层2
  tf.keras.layers.Dense(64, activation=tf.nn.relu),  #隐藏层3
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)   #输出层
])


#定义优化器，损失函数，训练效果中计算准确率
#Adam算法为训练选择优化器和sparse_categorical_crossentropy为损失函数：
model.compile(optimizer='adam',  #Adam算法为训练选择优化器
              loss='sparse_categorical_crossentropy',   #损失用交叉熵，速度会更快
              metrics=['accuracy'])    #计算准确率



# 打印网络参数
model.summary()



# 训练模型

model.fit(x_train, y_train, epochs=5)

# 验证模型：
loss,accuracy = model.evaluate(x_test,  y_test, verbose=2)


