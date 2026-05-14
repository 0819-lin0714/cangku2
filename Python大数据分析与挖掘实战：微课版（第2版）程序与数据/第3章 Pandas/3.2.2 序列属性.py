# -*- coding: utf-8 -*-
import pandas as pd       
s1=pd.Series([1,-2,2.3,'hq'])  #创建序列s1
va1=s1.values                 #获取序列s1中的值，赋给变量va1
in1=s1.index                  #获取序列s1中的索引，赋给变量in1
print(va1)                    #打印变量结果
print(in1)                     #打印变量结果


va2=list(va1)      #将va1变量通过list命令转化为列表，赋给变量va2
in2=list(in1)      #将in1变量通过list命令转化为列表,赋给变量in2
