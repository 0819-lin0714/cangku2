# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
plt.figure(1)               # 创建第一个画布
plt.subplot(2, 1, 1)         # 画布划分为2×1图形阵，选择第1张图片

import numpy as np
plt.figure(1)  # 创建画布
x = np.linspace(0, 1, 1000)
plt.subplot(2, 1, 1)  # 分为2×1图形阵，选择第1张图片绘图
plt.title('y=x^2 & y=x')  # 添加标题
plt.xlabel('x')  # 添加x轴名称‘x’
plt.ylabel('y')  # 添加y轴名称‘y’
plt.xlim((0, 1))  # 指定x轴范围（0,1）
plt.ylim((0, 1))  # 指定y轴范围（0,1）
plt.xticks([0, 0.3, 0.6, 1])  # 设置x轴刻度
plt.yticks([0, 0.5, 1])  # 设置y轴刻度
plt.plot(x, x ** 2)
plt.plot(x, x)
plt.legend(['y=x^2', 'y=x'])  # 添加图例
plt.savefig('1.png')  # 保存图片
plt.show()


