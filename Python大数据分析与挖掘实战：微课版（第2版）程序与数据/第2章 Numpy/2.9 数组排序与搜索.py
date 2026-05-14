# -*- coding: utf-8 -*-
import numpy as np
arr = np.array([5,2,3,3,1,9,8,6,7])
arr1=np.sort(arr)

arr = np.array([5,2,3,3,1,1,9,8,6,7,8,8])
arr1=arr.reshape(3,4)
maxindex=np.argmax(arr)
minindex=np.argmin(arr)
maxindex1=np.argmax(arr1,axis=0)#返回各列最大值索引
minindex1=np.argmin(arr1,axis=1)#返回各行最小值索引

