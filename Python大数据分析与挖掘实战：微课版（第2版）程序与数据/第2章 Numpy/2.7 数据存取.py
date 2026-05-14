# -*- coding: utf-8 -*-
import numpy as np
A=np.array([[1,2],[3,4]])     #定义二维数组A
B=np.array([[5,6],[7,8]])     #定义二维数组B
C_s=np.hstack((A,B))        #水平连接
np.save('data',C_s)

import numpy as np
C_s=np.load('data.npy')

