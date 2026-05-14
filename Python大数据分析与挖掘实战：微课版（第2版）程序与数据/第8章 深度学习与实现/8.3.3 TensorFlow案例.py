# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 00:29:36 2020

@author: Lukas
"""

# 产生数据
import tensorflow as tf
W = 3.0   # W参数设置
b =1.0    # b参数设置
num = 1000
# x随机输入
x = tf.random.normal(shape=[num])
# 随机偏差
c = tf.random.normal(shape=[num])
# 构造y数据
y = W * x + b + c
print(y)

# 画图观察
import matplotlib.pyplot as plt    #加载画图库
plt.scatter(x, y, c='b')    # 画离散图
plt.show()    # 展示图


#定义模型
class LineModel(object):   # 定义一个LineModel的类
    def __init__(self):
        # 初始化变量
        self.W = tf.Variable(5.0)
        self.b = tf.Variable(0.0)
        
    def __call__(self, x):   #定义返回值
        return self.W * x + self.b 

# 定义损失函数
def loss(predicted_y, true_y):   # 定义损失函数
    return tf.reduce_mean(tf.square(true_y -predicted_y))  # 返回均方误差值

# 定义训练
    
def train(model, x, y, learning_rate):   #定义训练函数
    # 记录loss计算过程
    with tf.GradientTape() as t:
        current_loss = loss(model(x), y)  #损失函数计算
        # 对W，b求导
        d_W, d_b = t.gradient(current_loss, [model.W, model.b])
        # 减去梯度*学习率
        model.W.assign_sub(d_W*learning_rate)  #减法操作
        model.b.assign_sub(d_b*learning_rate)

# 求解过程
        
model= LineModel()  #运用模型实例化
# 计算W，b参数值的变化
W_s, b_s = [], []    #增加新中间变量
for epoch in range(15):    #循环15次
    W_s.append(model.W.numpy())  #提取模型的W参数添加到中间变量w_s
    b_s.append(model.b.numpy())
    # 计算损失函数loss
    current_loss = loss(model(x), y)
    train(model,x, y, learning_rate=0.1)   # 运用定义的train函数训练
    print('Epoch %2d: W=%1.2f b=%1.2f, loss=%2.5f' %
        (epoch, W_s[-1], b_s[-1], current_loss))    #输出训练情况
# 画图，把W,b的参数变化情况画出来
epochs = range(15)   #这个迭代数据与上面循环数据一样
plt.plot(epochs, W_s, 'r',
         epochs, b_s, 'b')  #画图
plt.plot([W] * len(epochs), 'r--',
         [b] * len(epochs), 'b-*')
plt.legend(['pridect_W', 'pridet_b', 'true_W', 'true_b'])  # 图例
plt.show()
