# -*- coding: utf-8 -*-
#1.9.1
#定义函数
def sumt(t):
    s = 0
    while t:
       s=s+t
       t=t-1
#调用函数并打印结果       
s=sumt(50)
print(s)

#1.9.2
def sumt(t):
    s = 0
    while t:
       s=s+t
       t=t-1
    return s   
#调用函数并打印结果       
s=sumt(50)
print(s)

#1.9.3
#定义函数
def test(r):
    import math
    s=math.pi*r**2
    c=2*math.pi*r
    L=(s,c)
    D=[s,c,L]
    return (s,c,L,D)
#调用函数并打印结果
v=test(10)
s=v[0]
c=v[1]
L=v[2]
D=v[3]
print(s)
print(c)
print(L)
print(D)

