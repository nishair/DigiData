#Wilmington
f5 = data[data['deviceid']=='7f5f198']
f5.portid.unique()
f5.columns
FD = f5[['readingdate','temperature']]

a = FD.values

#Only coolers
FD = FD.sort_values('readingdate')
FD1 = FD.set_index('readingdate')
FD1.plot(figsize=(15,6))
plt.show() -- 3 excursions
result1 = adfuller(FD1['temperature'])
#FD2 = FD1.groupby(pd.Grouper(level='readingdate'))
a = pd.to_datetime(FD['readingdate']).apply(lambda x: x.date())
b = pd.DataFrame({'readingdate':a.values})
FD['readingdate'] = b['readingdate'].values
FD1 = FD.set_index('readingdate')
print(FD.to_string())
FD.std()
FD.mean()
split = int(len(FD) / 2)
FD1, FD2 = FD[0:split], FD[split:]
mean1, mean2 = FD1.mean(), FD2.mean()
var1, var2 = FD1.var(), FD2.var()
result = []
result = adfuller(FD['temperature'])

#RX
WF = data[data['deviceid']=='7a03fa1']
WF = WF[['readingdate','temperature']]
WF1 = WF.sort_values('readingdate')
WF2 = WF1.set_index('readingdate')

plt.figure(1)
plt.subplot(211)
plt.plot(FD1)
plt.subplot(212)
plt.plot(WF2)
plt.show()

split = int(len(WF2) / 2)
WF21, WF22 = WF2[0:split], WF2[split:]
mean1, mean2 = WF21.mean(), WF22.mean()
var1, var2 = WF21.var(), WF22.var()
result = []
result = adfuller(WF2['temperature'])
WF21.std()
WF22.std()
mean1
mean2
var1
var2
result

FDt = FD.to_string()


##SHALLOTTE
f4 = data[data['deviceid']=='742d9bd']
f41 = f4[['readingdate','temperature']]
Af41 = f41.sort_values('readingdate')
Aaf41 = Af41.set_index('readingdate')
Aaf41.plot(figsize=(15,6))
plt.show() -- 2 excursions
result2 = adfuller(Aaf41['temperature'])

split = int(len(WF2) / 2)
Aaf411, Aaf412 = Aaf41[0:split], Aaf41[split:]
mean1, mean2 = Aaf411.mean(), Aaf412.mean()
var1, var2 = Aaf411.var(), Aaf412.var()
result = []
result = adfuller(Aaf41['temperature'])
Aaf411.std()
Aaf412.std()
mean1
mean2
var1
var2
result

f6 = data[data['deviceid']=='a0a9b76']
f61 = f6[['readingdate','temperature']]
Af61 = f61.sort_values('readingdate')
Aaf61 = Af61.set_index('readingdate')
Aaf61.plot(figsize=(15,6))
plt.show() -- 2 excursions and a potential excursion

split = int(len(Aaf61) / 2)
Aaf611, Aaf612 = Aaf61[0:split], Aaf61[split:]
mean1, mean2 = Aaf611.mean(), Aaf612.mean()
var1, var2 = Aaf611.var(), Aaf612.var()
result = []
result = adfuller(Aaf61['temperature'])
Aaf611.std()
Aaf612.std()
mean1
mean2
var1
var2
result

SHF = data[data['deviceid']=='7c5e522']
SHF = SHF[['readingdate','temperature']]
SHF = SHF.sort_values('readingdate')
SHF = SHF.set_index('readingdate')

split = int(len(SHF) / 2)
SHF1, SHF2 = SHF[0:split], SHF[split:]
mean1, mean2 = SHF1.mean(), SHF2.mean()
var1, var2 = SHF1.var(), SHF2.var()
result = []
result = adfuller(SHF['temperature'])
SHF1.std()
SHF2.std()
mean1
mean2
var1
var2
result

import matplotlib.pyplot as plt

fig = plt.figure()
axes = fig.subplots(nrows=2, ncols=2)

plt.show()

import numpy as np
import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec

# Create 2x2 sub plots
gs = gridspec.GridSpec(2, 2)

pl.figure()
ax = pl.subplot(gs[0, 0]) # row 0, col 0
pl.plot(Aaf41)

ax = pl.subplot(gs[0, 1]) # row 0, col 1
pl.plot(Aaf61)

ax = pl.subplot(gs[1, :]) # row 1, span all columns
pl.plot(SHF)
plt.show()

pd.set_option('display.max_rows', 3000)

####INDIANA
f1 = data[data['deviceid']=='7f544be']
f11 = f1[['readingdate','temperature']]
Af11 = f11.sort_values('readingdate')
Aaf11 = Af11.set_index('readingdate')

split = int(len(Aaf11) / 2)
Aaf111, Aaf112 = Aaf11[0:split], Aaf11[split:]
mean1, mean2 = Aaf111.mean(), Aaf112.mean()
var1, var2 = Aaf111.var(), Aaf112.var()
result = []
result = adfuller(Aaf11['temperature'])
Aaf111.std()
Aaf112.std()
mean1
mean2
var1
var2
result

f2 = data[data['deviceid']=='a21ad0d']
f21 = f2[['readingdate','temperature']]
Af21 = f21.sort_values('readingdate')
Aaf21 = Af21.set_index('readingdate')

split = int(len(Aaf21) / 2)
Aaf211, Aaf212 = Aaf21[0:split], Aaf21[split:]
mean1, mean2 = Aaf211.mean(), Aaf212.mean()
var1, var2 = Aaf211.var(), Aaf212.var()
result = []
result = adfuller(Aaf21['temperature'])
Aaf211.std()
Aaf212.std()
mean1
mean2
var1
var2
result

f3 = data[data['deviceid']=='827588b']
f31 = f3[['readingdate','temperature']]
Af31 = f31.sort_values('readingdate')
Aaf31 = Af31.set_index('readingdate')

split = int(len(Aaf31) / 2)
Aaf311, Aaf312 = Aaf31[0:split], Aaf31[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(Aaf31['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result

fr1 = data[data['deviceid']=='704811e']
Fr11 = fr1.sort_values('readingdate')
FD111 = Fr11.set_index('readingdate')
FD1111 = FD111[['temperature']]

split = int(len(FD1111) / 2)
Aaf311, Aaf312 = FD1111[0:split], FD1111[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(FD1111['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result


fig = plt.figure()

plt.subplot(2, 2, 1)
plt.plot(Aaf11)

plt.subplot(2, 2, 2)
plt.plot(Aaf21)

plt.subplot(2, 2, 3)
plt.plot(Aaf31)

plt.subplot(2, 2, 4)
plt.plot(FD1111)

plt.show()

f13 = data[data['deviceid']=='742fb17']
f131 = f13[['readingdate','temperature']]
Af131 = f131.sort_values('readingdate')
Aaf131 = Af131.set_index('readingdate')
Aaf131.plot(figsize=(15,6))
plt.show() -- looks bad. Potentially could be broken. 

split = int(len(Aaf131) / 2)
Aaf311, Aaf312 = Aaf131[0:split], Aaf131[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(Aaf131['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result

f14 = data[data['deviceid']=='74338ec']
f141 = f14[['readingdate','temperature']]
Af141 = f141.sort_values('readingdate')
Aaf141 = Af141.set_index('readingdate')
Aaf141.plot(figsize=(15,6))
plt.show() --  one excursion

split = int(len(Aaf141) / 2)
Aaf311, Aaf312 = Aaf141[0:split], Aaf141[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(Aaf141['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result

f15 = data[data['deviceid']=='80b15ee']
f151 = f15[['readingdate','temperature']]
Af151 = f151.sort_values('readingdate')
Aaf151 = Af151.set_index('readingdate')
Aaf151.plot(figsize=(15,6))
plt.show() -- bunch of excursions

split = int(len(Aaf151) / 2)
Aaf311, Aaf312 = Aaf151[0:split], Aaf151[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(Aaf151['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result

gs = gridspec.GridSpec(2, 2)

pl.figure()
ax = pl.subplot(gs[0, 0]) # row 0, col 0
pl.plot(Aaf131)

ax = pl.subplot(gs[0, 1]) # row 0, col 1
pl.plot(Aaf141)

ax = pl.subplot(gs[1, :]) # row 1, span all columns
pl.plot(Aaf151)
plt.show()

FBN = data[data['deviceid']=='723373e']
FBN = FBN[['readingdate','temperature']]
FBN = FBN.sort_values('readingdate')
FBN = FBN.set_index('readingdate')

split = int(len(FBN) / 2)
Aaf311, Aaf312 = FBN[0:split], FBN[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(FBN['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result


ABN = data[data['deviceid']=='73d8ffa']
ABN = ABN[['readingdate','temperature']]
ABN = ABN.sort_values('readingdate')
ABN = ABN.set_index('readingdate')

split = int(len(ABN) / 2)
Aaf311, Aaf312 = ABN[0:split], ABN[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(ABN['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result

plt.figure(1)
plt.subplot(211)
plt.plot(FBN)
plt.subplot(212)
plt.plot(ABN)
plt.show()

ATX1 = data[data['deviceid']=='73d82b1']
ATX1 = ATX1[['readingdate','temperature']]
ATX1 = ATX1.sort_values('readingdate')
ATX1 = ATX1.set_index('readingdate')

split = int(len(ATX1) / 2)
Aaf311, Aaf312 = ATX1[0:split], ATX1[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(ATX1['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result


ATX2 = data[data['deviceid']=='7430a41']
ATX2 = ATX2[['readingdate','temperature']]
ATX2 = ATX2.sort_values('readingdate')
ATX2 = ATX2.set_index('readingdate')

split = int(len(ATX2) / 2)
Aaf311, Aaf312 = ATX2[0:split], ATX2[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(ATX2['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result

plt.figure(1)
plt.subplot(211)
plt.plot(ATX1)
plt.subplot(212)
plt.plot(ATX2)
plt.show()


f7 = data[data['deviceid']=='7f5331e']
f71 = f7[['readingdate','temperature']]
Af71 = f71.sort_values('readingdate')
Aaf71 = Af71.set_index('readingdate')
Aaf71.plot(figsize=(15,6))
plt.show() -- no excursions but potentially the device is degrading

split = int(len(Aaf71) / 2)
Aaf311, Aaf312 = Aaf71[0:split], Aaf71[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(Aaf71['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result

f8 = data[data['deviceid']=='7f50eb9']
f81 = f8[['readingdate','temperature']]
Af81 = f81.sort_values('readingdate')
Aaf81 = Af81.set_index('readingdate')
Aaf81.plot(figsize=(15,6))
plt.show() -- no excursions but after a surge till 8 there are some changes

split = int(len(Aaf81) / 2)
Aaf311, Aaf312 = Aaf81[0:split], Aaf81[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(Aaf81['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result

f9 = data[data['deviceid']=='7511c07']
f91 = f9[['readingdate','temperature']]
Af91 = f91.sort_values('readingdate')
Aaf91 = Af91.set_index('readingdate')
Aaf91.plot(figsize=(15,6))
plt.show() -- Potentially broken since everything is above 8

split = int(len(Aaf91) / 2)
Aaf311, Aaf312 = Aaf91[0:split], Aaf91[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(Aaf91['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result

gs = gridspec.GridSpec(2, 2)

pl.figure()
ax = pl.subplot(gs[0, 0]) # row 0, col 0
pl.plot(Aaf71)

ax = pl.subplot(gs[0, 1]) # row 0, col 1
pl.plot(Aaf81)

ax = pl.subplot(gs[1, :]) # row 1, span all columns
pl.plot(Aaf91)
plt.show()

f10 = data[data['deviceid']=='7f7ca60']
f101 = f10[['readingdate','temperature']]
Af101 = f101.sort_values('readingdate')
Aaf101 = Af101.set_index('readingdate')
Aaf101.plot(figsize=(15,6))
plt.show() -- no excursions

split = int(len(Aaf101) / 2)
Aaf311, Aaf312 = Aaf101[0:split], Aaf101[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(Aaf101['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result


f11 = data[data['deviceid']=='810a060']
f111 = f11[['readingdate','temperature']]
Af111 = f111.sort_values('readingdate')
Aaf111 = Af111.set_index('readingdate')
Aaf111.plot(figsize=(15,6))
plt.show() -- One excursion

split = int(len(Aaf111) / 2)
Aaf311, Aaf312 = Aaf111[0:split], Aaf111[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(Aaf111['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result


f12 = data[data['deviceid']=='80acce5']
f121 = f12[['readingdate','temperature']]
Af121 = f121.sort_values('readingdate')
Aaf121 = Af121.set_index('readingdate')
Aaf121.plot(figsize=(15,6))
plt.show() -- one huge one small

split = int(len(Aaf121) / 2)
Aaf311, Aaf312 = Aaf121[0:split], Aaf121[split:]
mean1, mean2 = Aaf311.mean(), Aaf312.mean()
var1, var2 = Aaf311.var(), Aaf312.var()
result = []
result = adfuller(Aaf121['temperature'])
Aaf311.std()
Aaf312.std()
mean1
mean2
var1
var2
result

gs = gridspec.GridSpec(2, 2)

pl.figure()
ax = pl.subplot(gs[0, 0]) # row 0, col 0
pl.plot(Aaf101)

ax = pl.subplot(gs[0, 1]) # row 0, col 1
pl.plot(Aaf111)

ax = pl.subplot(gs[1, :]) # row 1, span all columns
pl.plot(Aaf121)
plt.show()
