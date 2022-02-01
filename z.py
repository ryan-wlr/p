import pandas as pd 
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


a = pd.read_csv('challenge_30-days_sofar_20210530_atlantic_sample.csv', header=None)
c = np.array(a)

v = np.arange(51889.0).reshape(51889)
a = np.arange(103778).reshape(51889,2)



for x in (n+1 for n in range(51888)):
    df = pd.DataFrame({'time': [pd.to_datetime(c[x,7])]})
    df_unix_sec = pd.to_datetime(df['time']).astype(int)/10**9
    d = (df_unix_sec/3600)
    v[x-1] = d
    
    
y = np.arange(311334.0).reshape(51889,6)
y[0:51888,1] = c[1:51889,8]
y[0:51888,2] = c[1:51889,9]
y[0:51888,0] = v[0:51888]

#Calculate time to digits
for x in range(51888):
    a[x] = y[x+1,0]-y[x,0]
    a[x] = a[x] + x 

#Calculate distance in coordinates    
for x in range(51888):
    a[x,1] = np.sqrt((np.square((y[x+1,1]-y[x,1])) + np.square((y[x+1,2]-y[x,2])))) 


mod = KNeighborsRegressor()

x_train = np.arange(51889.0).reshape(51889)
y_train = np.arange(51889.0).reshape(51889)

x_train = a[0:51889,0]
y_train = a[0:51889,1]

x_train= x_train.reshape(-1, 1)
y_train= y_train.reshape(-1, 1)


mod.fit(x_train,y_train)

pred = mod.predict(x_train)

plt.scatter(pred,y_train)

plt.show()
