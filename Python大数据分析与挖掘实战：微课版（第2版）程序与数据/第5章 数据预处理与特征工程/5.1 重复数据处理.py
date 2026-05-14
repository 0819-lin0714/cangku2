import pandas as pd
dict1={'code':['A01','A01','A01','A02','A02','A02','A01','A01'],
       'month':['01','02','03','01','02','03','01','02'],
       'price':[10,12,13,15,17,20,10,12]}
df1=pd.DataFrame(dict1)
df2=df1.drop_duplicates() 

