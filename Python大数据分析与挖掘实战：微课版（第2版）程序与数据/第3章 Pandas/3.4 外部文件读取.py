import pandas as pd
path='一、车次上车人数统计表.xlsx';
data=pd.read_excel(path);
data=pd.read_excel(path,'Sheet2')  #读取sheet里面的数据
dta=pd.read_excel('dta.xlsx',header=None)  #无表头

dta1=pd.read_table('txt1.txt',header=None)  #分隔默认为Tab键，设置无表头。
dta2=pd.read_table('txt2.txt',sep='\s+')                #分隔为空格，带头头
dta3=pd.read_table('txt3.txt',sep=',',header=None)  #分隔为逗号，设置无表头

#3.4.3
import pandas as pd
A=pd.read_csv('data.csv',sep=',');#道号分隔
#A=pd.read_csv('data.csv',sep=',',nrows=1000)

reader=pd.read_csv('data.csv',sep=',',chunksize=50000,usecols=[3,4,10])
k=0
for A in reader:
    k=k+1
    print('第'+str(k)+'次读取数据规模为： ',len(A))