import pandas as pd
from statsmodels.tsa.stattools import adfuller
import scipy
from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
from matplotlib import pyplot as plt
from pandas import concat
import matplotlib as plt
import calmap


mdata = pd.read_csv("metadata.csv")
data = pd.read_csv("readings.csv")

##FREEZERS
fr1 = data[data['deviceid']=='704811e']
Fr11 = fr1.sort_values('readingdate')
FD111 = Fr11.set_index('readingdate')
FD1111 = FD111[['temperature']]
FD1111.plot(figsize=(15,6))

fr1 = data[data['deviceid']=='7c5e522']
Fr11 = fr1.sort_values('readingdate')
FD111 = Fr11.set_index('readingdate')
FD1111 = FD111[['temperature']]
FD1111.plot(figsize=(15,6))

fr1 = data[data['deviceid']=='7a03fa1']
Fr11 = fr1.sort_values('readingdate')
FD111 = Fr11.set_index('readingdate')
FD1111 = FD111[['temperature']]
FD1111.plot(figsize=(15,6))

for key, item in test:
	print(test.get_group(key), "\n\n")

##COOOLERS -- 



f1 = data[data['deviceid']=='7f544be']
f11 = f1[['readingdate','temperature']]
Af11 = f11.sort_values('readingdate')
Aaf11 = Af11.set_index('readingdate')
Aaf11.plot(figsize=(15,6))
plt.show() -- 0 excursions
Aaf11.hist() 
plt.show()
split = int(len(Af11) / 2)
Af111, Af112 = Af11[0:split], Af11[split:]
mean1, mean2 = Af111.mean(), Af112.mean()
var1, var2 = Af111.var(), Af112.var()
result = []
result = adfuller(Aaf11['temperature'])

f2 = data[data['deviceid']=='a21ad0d']
f21 = f2[['readingdate','temperature']]
Af21 = f21.sort_values('readingdate')
Aaf21 = Af21.set_index('readingdate')
Aaf21.plot(figsize=(15,6))
plt.show() -- 0 excursions

f3 = data[data['deviceid']=='827588b']
f31 = f3[['readingdate','temperature']]
Af31 = f31.sort_values('readingdate')
Aaf31 = Af31.set_index('readingdate')
Aaf31.plot(figsize=(15,6))
plt.show() -- 0 excursions --a lot of values hitting 8
result2 = adfuller(Aaf31['temperature'])

f4 = data[data['deviceid']=='742d9bd']
f41 = f4[['readingdate','temperature']]
Af41 = f41.sort_values('readingdate')
Aaf41 = Af41.set_index('readingdate')
Aaf41.plot(figsize=(15,6))
plt.show() -- 2 excursions
result2 = adfuller(Aaf41['temperature'])

f6 = data[data['deviceid']=='a0a9b76']
f61 = f6[['readingdate','temperature']]
Af61 = f61.sort_values('readingdate')
Aaf61 = Af61.set_index('readingdate')
Aaf61.plot(figsize=(15,6))
plt.show() -- 2 excursions and a potential excursion

f7 = data[data['deviceid']=='7f5331e']
f71 = f7[['readingdate','temperature']]
Af71 = f71.sort_values('readingdate')
Aaf71 = Af71.set_index('readingdate')
Aaf71.plot(figsize=(15,6))
plt.show() -- no excursions but potentially the device is degrading

f8 = data[data['deviceid']=='7f50eb9']
f81 = f8[['readingdate','temperature']]
Af81 = f81.sort_values('readingdate')
Aaf81 = Af81.set_index('readingdate')
Aaf81.plot(figsize=(15,6))
plt.show() -- no excursions but after a surge till 8 there are some changes

f9 = data[data['deviceid']=='7511c07']
f91 = f9[['readingdate','temperature']]
Af91 = f91.sort_values('readingdate')
Aaf91 = Af91.set_index('readingdate')
Aaf91.plot(figsize=(15,6))
plt.show() -- Potentially broken since everything is above 8

f10 = data[data['deviceid']=='7f7ca60']
f101 = f10[['readingdate','temperature']]
Af101 = f101.sort_values('readingdate')
Aaf101 = Af101.set_index('readingdate')
Aaf101.plot(figsize=(15,6))
plt.show() -- no excursions

f11 = data[data['deviceid']=='810a060']
f111 = f11[['readingdate','temperature']]
Af111 = f111.sort_values('readingdate')
Aaf111 = Af111.set_index('readingdate')
Aaf111.plot(figsize=(15,6))
plt.show() -- One excursion

f12 = data[data['deviceid']=='80acce5']
f121 = f12[['readingdate','temperature']]
Af121 = f121.sort_values('readingdate')
Aaf121 = Af121.set_index('readingdate')
Aaf121.plot(figsize=(15,6))
plt.show() -- one huge one small



f15 = data[data['deviceid']=='80b15ee']
f151 = f15[['readingdate','temperature']]
Af151 = f151.sort_values('readingdate')
Aaf151 = Af151.set_index('readingdate')
Aaf151.plot(figsize=(15,6))
plt.show()

result = adfuller(Aaf11['temperature'])[0]


import pandas as pd
from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
from matplotlib import pyplot
series = pd.read_csv('daily-minimum-temperatures.csv', header=0)
groups = series.groupby(TimeGrouper('A'))
years = DataFrame()
for name, group in groups:
	years[name.year] = group.values
years = years.T
pyplot.matshow(years, interpolation=None, aspect='auto')
pyplot.show()


plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
