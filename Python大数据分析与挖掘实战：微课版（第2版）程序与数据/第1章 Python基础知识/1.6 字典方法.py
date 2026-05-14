# -*- coding: utf-8 -*-
d=dict()  #产生空字典
D={}     #产生空字典
list1=[('a','ok'),('1','lk'),('001','lk')]   #嵌套元素为元组
list2=[['a','ok'],['b','lk'],[3,'lk']]   #嵌套元素为列表
d1=dict(list1)
d2=dict(list2)
print('d=：',d)
print('D=: ',D) 
print('d1=: ',d1)
print('d2=: ',d2)

print(d2.get('b'))

d.setdefault('a',0)
D.setdefault('b',[1,2,3,4,5])
print(d)
print(D)

