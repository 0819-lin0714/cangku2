# -*- coding: utf-8 -*-
#1.7.1
x=10
import math                        #导入数学函数库
if x>0:                             #冒号
  s=math.sqrt(x)                 #求平方根，缩进
  print('s= ',s)                   #打印结果，缩进

#1.7.2
x=-10
import math                        #导入数学函数库
if x>0:                             # 冒号
  s=math.sqrt(x)                 #求平方根，缩进
  print('s= ',s)                   #打印结果，缩进
else:
  s='负数不能求平方根'          #提示语，缩进
  print('s= ',s)                   #打印结果，缩进

#1.7.3
weather = 'sunny'
if weather =='sunny':
    print ("shopping")
elif weather =='cloudy':
    print ("playing football")
else:
    print ("do nothing")
