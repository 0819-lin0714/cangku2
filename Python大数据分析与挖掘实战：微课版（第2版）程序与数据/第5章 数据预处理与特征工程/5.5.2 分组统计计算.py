import pandas as pd
B=pd.read_excel('表5-1 用户消费数据.xlsx')
B1=B.groupby(['姓名','日期'])['消费额'].sum()
B['总消费额']=B.groupby(['姓名','日期'])['消费额'].transform('sum')
B['消费占比']=B['消费额'].values/B['总消费额'].values

