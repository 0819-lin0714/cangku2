# -*- coding: utf-8 -*-
#1.5.1
L1=[1,2,3,4,5,6]      
L2=[1,2,'HE',3,5]
L3=['KJ','CK','HELLO']
L4=[1,4,2,3,8,4,7]

L=list()  #产生空列表L
L=[]    #也可以用[]来产生空列表

L1.append('H')  # 在L1列表后面增加元素‘H’.
print(L1)
for t in L2:        #利用循环,将L2中的元素，依次顺序添加到前面新建的空列表L中
    L.append(t)    
print(L)

L1.extend(L2)  # 在前面的L1基础上，添加整个L2至其后面
print(L1)

print('元素2出现的次数为：',L1.count(2))   

print('H的索引下标为：',L1.index('H'))

L1.remove('HE') #删除HE元素
print(L1)

L4.sort()
print(L4)

L4[2]=10
print(L4)

t=(1,2,3,4)
#t[2]=10       #报错
