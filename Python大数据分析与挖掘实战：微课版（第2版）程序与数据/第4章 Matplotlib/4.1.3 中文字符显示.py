# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 10, 0.2)
y = np.sin(x)
plt.title('sin曲线')
plt.plot(x, y)
plt.savefig('2.png')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 10, 0.2)
y = np.sin(x)
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号“-”显示异常
plt.title('sin曲线')
plt.plot(x, y)
plt.savefig('2.png')
plt.show()


