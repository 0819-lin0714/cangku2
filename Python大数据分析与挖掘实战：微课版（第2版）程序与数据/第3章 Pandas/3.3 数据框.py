# -*- coding: utf-8 -*-
##3.3
#3.3.1
import pandas as pd
import numpy as np
data={'a':[2,2,np.nan,5,6],'b':['kl','kl','kl',np.nan,'kl'],'c':[4,6,5,np.nan,6],'d':[7,9,np.nan,9,8]}
df=pd.DataFrame(data)

#3.3.2
print('columns= ')
print(df.columns)
print('-'*50)
print('index= ')
print(df.index)
print('-'*50)
print('values= ')
print(df.values)

#3.3.3
df1=df.dropna()

df2=df.fillna(0)       #所有空值元素填充0
df3=df.fillna('Kl')      #所有空值元素填充kl
df4=df.fillna({'a':0,'b':'kl','c':0,'d':0})   #全部列填充
df5=df.fillna({'a':0,'b':'kl'})    #部分列填充

data={'a':[5,3,4,1,6],'b':['d','c','a','e','q'],'c':[4,6,5,5,6]}
Df=pd.DataFrame(data)
Df1=Df.sort_values('a',ascending=False) #默认按升序，这里设置为降序

Df2=Df1.sort_index(ascending=False)  #默认按升序，这里设置为降序

H4=Df2.head(4);

H41=H4.drop('b',axis=1) #需指定轴为1

Df3=pd.DataFrame({'d':[1,2,3,4,5]})
Df4=Df.join(Df3)

list1=['a','b','c','d','e','f']
list2=[1,2,3,4,5,6]
list3=[1.4,3.5,2,6,7,8]
list4=[4,5,6,7,8,9]
list5=['t',5,6,7,'k',9.6]
D={'M1':list1,'M2':list2,'M3':list3,'M4':list4,'M5':list5}  #定义字典D，值为字符、数值混合数据
G={'M1':list2,'M2':list3,'M3':list4}                  #定义字典G，值为纯数值数据
D=pd.DataFrame(D)                             #将字典D转化为数据框
D1=D.values                              #将数据框D转化为Numpy数组D1
G=pd.DataFrame(G)                             #将字典G转化为数据框
G1=G.values                               #将数据框G转化为Numpy数组G1

print(D1)

D.to_excel('D.xlsx')
G.to_excel('G.xlsx')

Dt=Df4.drop('b',axis=1)   #Df4中删除b列
R1=Dt.sum()           #各列求和
R2=Dt.mean()      #各列求平均值
R3=Dt.describe()   #各列做描述性统计

#3.3.4
# iloc for positional indexing
c3=df2.iloc[1:3,2]
c4=df2.iloc[1:3,0:2]
c5=df2.iloc[1:3,:]
c6=df2.iloc[[0,2,3],[1,2]]
TF=[True,False,False,True,True]
c7=df2.iloc[TF,[1]]

# loc for label based indexing
c8=df2.loc[df2['b'] == 'kl',:];
c9=df2.loc[df2['b'] == 'kl',:].head(3);
c10=df2.loc[df2['b'] == 'kl',['a','c']].head(3);
c11=df2.loc[df2['b'] == 'kl',['a','c']];
