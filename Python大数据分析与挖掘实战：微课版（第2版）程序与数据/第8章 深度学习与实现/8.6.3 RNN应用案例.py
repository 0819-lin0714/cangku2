# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 17:50:46 2020

@author: Lukas
"""
#加载需要用到的模块

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Embedding, LSTM, Bidirectional
from tensorflow.keras.datasets import imdb
import tensorflow as tf

# 词汇表收录的单词数，
max_features = 10000
# 一个句子长度
maxlen = 100
# 一个批次数据量大小
batch_size = 32
# 加载数据,评论文本已转换为整数，其中每个整数表示字典中的特定单词
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)


# 循环神经网络输入长度固定
#这里应该注意，循环神经网络的输入是固定长度的，否则运行后会出错。
#由于电影评论的长度必须相同，pad_sequences 函数来标准化评论长度
x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen)



#定义嵌入层

model = Sequential()
# 嵌入层
model.add(Embedding(max_features,  # 词汇表大小中收录单词数量，也就是嵌入层矩阵的行数
                    128,           # 每个单词的维度，也就是嵌入层矩阵的列数
                    input_length=maxlen)) # 一篇文本的长度

# 定义LSTM隐藏层
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
# 模型输出层
model.add(Dense(1, activation='sigmoid'))



# 模型编译
model.compile(loss='binary_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])

model.summary()


# 训练过程

model.fit(x_train, y_train,
          batch_size=batch_size,            # 遍历1遍数据集的批次数=len(x_train)/batch_size
          epochs=5,                         # 只遍历整个数据集4遍
          validation_data=[x_train, y_train]) # 验证集


#模型验证
results = model.evaluate(x_test, y_test)
print(results)
'''
#模型的画图表示
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
from keras.utils import plot_model
plot_model(model,to_file='RNN-IMDB.png',show_shapes=True)
RI = mpimg.imread('RNN-IMDB.png') # 读取和代码处于同一目录下的RNN-IMDB.png
plt.imshow(RI) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()
'''


