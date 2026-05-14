import pandas as pd
t1=pd.to_datetime('2015-08-01 05:50:43.000001',format='%Y-%m-%d %H:%M:%S.%f')
t2=pd.to_datetime(['2015-08-01 05:50:43','2015-08-01 05:51:40'])
t3=pd.to_datetime(['2015-08-01','2015-08-02'])
t4=pd.to_datetime(pd.Series(['2015-08-01','2015-08-02']))
