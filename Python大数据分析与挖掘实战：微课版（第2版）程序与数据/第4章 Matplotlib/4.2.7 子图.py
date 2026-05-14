# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  #导入绘图库中的pyplot模块，并且简称为plt。
#读取数据
path='一、车次上车人数统计表.xlsx';
data=pd.read_excel(path);
#筛选数据
tb=data.loc[data['车次'] == 'D02',['日期','上车人数']];
tb=tb.sort_values('日期');
tb1=data.loc[data['车次'] == 'D03',['日期','上车人数']];
tb1=tb1.sort_values('日期');
#构造绘图所需的横轴数据列和纵轴数据列
x=np.arange(1,len(tb.iloc[:,0])+1)
y1=tb.iloc[:,1]
y2=tb1.iloc[:,1]
plt.rcParams['font.sans-serif'] = 'SimHei'     # 设置字体为SimHei
plt.figure('子图')
plt.figure(figsize=(10,8))

plt.subplot(3,2,1)
plt.scatter(x,y1)
plt.xlabel('日期')
plt.ylabel('上车人数')
plt.xticks([1,5,10,15,20,24], tb['日期'].values[[0,4,9,14,19,23]], rotation = 45) 
plt.title('D02车次上车人数散点图')

plt.subplot(3,2,2)
plt.plot(x,y1,'r*--')  
plt.plot(x,y2,'b*--')  
plt.xlabel('日期')
plt.ylabel('上车人数')
plt.title('上车人数走势图')
plt.legend(['D02','D03'])
plt.xticks([1,5,10,15,20,24], tb['日期'].values[[0,4,9,14,19,23]], rotation = 45)

plt.subplot(3,2,3)
plt.bar(x,y1)
plt.xlabel('日期')
plt.ylabel('上车人数')
plt.title('D02车次上车人数柱状图')
plt.xticks([1,5,10,15,20,24], tb['日期'].values[[0,4,9,14,19,23]], rotation = 45)

plt.subplot(3,2,4)
plt.hist(y1)
plt.xlabel('上车人数')
plt.ylabel('频数')
plt.title('D02车次上车人数直方图')

plt.subplot(3,2,5)
D=data.iloc[:,0]
D=list(D.unique())  #车次号D02~D06
list1=[]    #预定义每个车次的上车人数列表
for d in D:
    dt=data.loc[data['车次'] == d,['上车人数']]
    s=dt.sum()
    list1.append(s['上车人数']) #或者s[0]
plt.pie(list1,labels=D,autopct='%1.2f%%') #绘制饼图，百分比保留小数点后两位
plt.title('各车次上车人数百分比饼图')

plt.subplot(3,2,6)
plt.boxplot([y1.values,y2.values])
plt.xticks([1,2], ['D02','D03'], rotation = 0) 
plt.title('D02、D03车次上车人数箱线图')
plt.ylabel('上车人数')
plt.xlabel('车次')
plt.tight_layout()
plt.savefig('子图')


