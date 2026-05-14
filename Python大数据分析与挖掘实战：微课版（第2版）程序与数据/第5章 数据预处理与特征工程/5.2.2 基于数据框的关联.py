import pandas as pd
#定义两个字典
dict1={'code':['A01','A01','A01','A02','A02','A02','A03','A03'],
       'month':['01','02','03','01','02','03','01','02'],
       'price':[10,12,13,15,17,20,10,9]}
dict2={'code':['A01','A01','A01','A02','A02','A02'],
       'month':['01','02','03','01','02','03'],
       'vol':[10000,10110,20000,10002,12000,21000]}
#对两个字典转换为数据框
df1=pd.DataFrame(dict1)
df2=pd.DataFrame(dict2)
del dict1,dict2
df_inner=pd.merge(df1,df2,how='inner',on=['code','month'])	#内连接
df_left=pd.merge(df1,df2,how='left',on=['code','month'])  	#左连接
df_right=pd.merge(df1,df2,how='right',on=['code','month']) 	#右连接
