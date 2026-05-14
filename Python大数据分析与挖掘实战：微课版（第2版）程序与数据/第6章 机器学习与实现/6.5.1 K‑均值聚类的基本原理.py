def K_mean(data,knum):
    #输入：data—聚类特征数据集，数据结构要求为NumPy数值数组
    #输入：knum—聚类个数
    #返回值，data后面加一列类别，显示类别
    import pandas as pd
    import numpy as np
    p=len(data[0,:])                        	#聚类数据维度
    cluscenter=np.zeros((knum,p))        	#预定义元素为全0的初始聚类中心
    lastcluscenter=np.zeros((knum,p))   	#预定义元素为全0的旧聚类中心
    #初始聚类中心和旧聚类中心初始化，取数据的前knum行作为初始值
    for i in range(knum):
      cluscenter[i,:]=data[i,:]
      lastcluscenter[i,:]=data[i,:]
    #预定义聚类类别一维数组，用于存放每次计算样本的所属类别
    clusindex=np.zeros((len(data)))
    while 1:
        for i in range(len(data)):
              #计算第i个样本到各个聚类中心的欧氏距离
              #预定义sumsquare，用于存放第i个样本到各个聚类中心的欧氏距离
              sumsquare=np.zeros((knum))
              for k in range(knum):
                  sumsquare[k]=sum((data[i,:]-cluscenter[k,:])**2)
              sumsquare=np.sqrt(sumsquare)
              #对第i个样本到各个聚类中心的欧氏距离进行升序排序
              s=pd.Series(sumsquare).sort_values()
              #判断第i个样本的类归属（距离最小，即s序列中第0个位置的索引）
              clusindex[i]=s.index[0]
        #将聚类结果添加到聚类数据最后一列
        clusdata=np.hstack((data,clusindex.reshape((len(data),1))))
        #更新聚类中心，新的聚类中心为对应类别样本特征的均值
        for i in range(knum):
              cluscenter[i,:]=np.mean(clusdata[clusdata[:,p]==i,:-1],0).reshape (1,p)
        #新的聚类中心与旧的聚类中心相减
        t=abs(lastcluscenter-cluscenter)
        #如果新的聚类中心与旧的聚类中心一致，即聚类中心不发生变化
        #返回聚类结果，并退出循环
        if sum(sum(t))==0:    
            return clusdata
            break
        #如果更新的聚类中心与旧的聚类中心不一致
        #将更新的聚类中心赋给旧的聚类中心，进入下一次循环
        else:
            for k in range(knum):
                lastcluscenter[k,:]=cluscenter[k,:]  

import pandas as pd
D=pd.read_excel('D.xlsx',header=None)
D=D.values
r=K_mean(D,2)
x0=r[r[:,2]==0,0]
y0=r[r[:,2]==0,1]
x1=r[r[:,2]==1,0]
y1=r[r[:,2]==1,1]
import matplotlib.pyplot as plt
plt.plot(x0,y0,'r*')  
plt.plot(x1,y1,'bo')  

