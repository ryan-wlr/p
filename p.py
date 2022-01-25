import pandas as pd 
import numpy as np
from dateutil.parser import parse
from datetime import datetime
from pandas.tseries.offsets import Hour, Minute


datestrs = ['7/6/2011', '8/6/2011']
idx = pd.to_datetime(datestrs + [None])
#print(idx)
#df = pd.DataFrame({'year':[2015, 2016], 'month':[2,3], 'day':[4,5]})
#pd.to_datetime(df)
#dtype: datetime64[minute]
#print(df)


a = pd.read_csv('challenge_30-days_sofar_20210530_atlantic_sample.csv', header=None)

c = np.array(a)
print(c[1:10,7])


#print(Hour(4))

'''
df = pd.DataFrame({'time': [pd.to_datetime('2019-01-15 13:25:43')]})
df_unix_sec = pd.to_datetime(df['time']).astype(int)/10**9
'''

v = np.arange(51889.0).reshape(51889)
for x in (n+1 for n in range(51888)):
    df = pd.DataFrame({'time': [pd.to_datetime(c[x,7])]})
    df_unix_sec = pd.to_datetime(df['time']).astype(int)/10**9
    d = (df_unix_sec/3600)
    v[x-1] = d

#print(v[:])

print(pd.Timestamp(1547559000, unit='s'))



#c.apply(lambda x:x.value)



#print(pd.Timestamp(429877.428611, unit='h'))
print(pd.Timestamp(450648.280278, unit='h'))

y = np.arange(311334.0).reshape(51889,6)
y[0:51888,1] = c[1:51889,8]
y[0:51888,2] = c[1:51889,9]
y[0:51888,0] = v[0:51888]
print(y)
a = np.arange(51889).reshape(51889,1)

for x in range(51888):
    a[x] = y[x+1,0]-y[x,0]
    
print(a[:])
np.savetxt("foo.csv", a, delimiter=",")
'''
s1 = pd.Series([0, 1, 2 ,3], index=['a','b','c','d'])
print(s1)

df_single_level_cols = pd.DataFrame([[0, 1], [2, 3]], index=['cat', 'dog'], columns=['weight', 'height'])
df_single_level_cols.stack()
print(df_single_level_cols)
z=np.array(df_single_level_cols)
#data = DataFrame({'k1': ['one'] * 3 + ['two'] * 4, 'k2': [1, 1, 2, 3, 3, 4, 4]})
#print(DataFrame)


data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}


data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
print(data[:])
data['food'].map(lambda x: meat_to_animal[x.lower()])
print(data[:])

data3 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'],columns=['one', 'two', 'three', 'four'])
print(data3[:])

''
y = np.arange(42).reshape(6,7)

print(y[2][0:3])
s = np.sum([0.5, 1.5])
print(s)

a = np.sum([[0, 1], [np.nan, 5]], where=[False, True], axis=1)

print(a)'''
