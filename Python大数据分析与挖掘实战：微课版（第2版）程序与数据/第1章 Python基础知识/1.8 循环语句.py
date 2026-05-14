# -*- coding: utf-8 -*-
#1.8.1
t = 100
s = 0
while t:
    s=s+t
    t=t-1
print ('s= ',s)

#1.8.2
list1=list()
list2=list()
list3=list()
for a in range(10):
    list1.append(a)
for t in ['a','b','c','d']:
    list2.append(t)
for q in ('k','j','p'):
    list3.append(q)
print(list1)
print(list2)
print(list3)

