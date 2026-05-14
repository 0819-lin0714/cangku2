# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:39:10 2020

@author: Administrator
"""
T1=(1,2,2,4,5)
T2=('H2',3,'KL')

t1=tuple()   #产生空元组
t=()        #产生空元组

print('元素2出现的次数为：',T1.count(2))

print('KL的下标索引为：',T2.index('KL'))

T3=T1+T2
print(T3)

