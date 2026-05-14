# 3.日期数据及时间元素提取
import pandas as pd
data=pd.read_excel('dat.xlsx')

data['刷卡时间']=pd.to_datetime(data.iloc[:,1],format='%Y-%m-%d %H:%M:%S.%f')
data['year']=data['刷卡时间'].dt.year
data['month']=data['刷卡时间'].dt.month
data['day']=data['刷卡时间'].dt.day
data['hour']=data['刷卡时间'].dt.hour
data['minute']=data['刷卡时间'].dt.minute
data['second']=data['刷卡时间'].dt.second
data['week']=data['刷卡时间'].dt.isocalendar().week
data['weekday']=data['刷卡时间'].dt.weekday













dict_map={'进站':1,'出站':0}
data['刷卡类型']=data['刷卡类型'].map(dict_map)
data1=data.iloc[data['刷卡类型'].values==1,[0,5,6]] #提取刷卡类型、hour、minute列
data1_hour=data1.groupby('hour')['刷卡类型'].sum()   #按hour分组，对刷卡类型列求和

bins=[0,100,500,1000]
dt1=pd.cut(data1_hour,bins)
dt2=pd.cut(data1_hour,bins,labels=[0,1,2])
dt_cut=pd.DataFrame({'c1':data1_hour.values,'c2':dt1.values,'c3':dt2.values})
dt_cut.index=data1_hour.index

