import pandas as pd
data=pd.read_excel('农村居民人均可支配收入来源2016.xlsx')
X=data.iloc[:,1:]
from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()
scaler.fit(X) 
X=scaler.transform(X) 
from sklearn.cluster import KMeans   
model = KMeans(n_clusters = 4, random_state=0, max_iter = 500) 
model.fit(X) 
c=model.labels_
Fs=pd.Series(c,index=data['地区'])
Fs=Fs.sort_values(ascending=True)

