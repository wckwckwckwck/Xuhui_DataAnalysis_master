
import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import folium



posi=pd.read_excel("上海体育馆进出站客流_201905.xlsx")

sheet2=pd.read_excel("上海体育馆进出站客流_201905.xlsx",sheet_name='一号线',skiprows = [0,1])
data1=sheet2.iloc[21].values
data2 = sheet2.iloc[21].values
d1 = []
d2 = []

for i in range(len(data1)):
    if i == 0:
        continue
    elif i % 2:
        d1.append(data1[i])
    else:
        d2.append(data1[i])
print(d1)
print(d2)
plt.title = '上海体育馆'
d1_xy=[]
d2_xy=[]
for i in range(1, 30):
    d1_xy.append((i, d1[i]))
    d2_xy.append((i, d2[i]))
print(d1_xy)
print(d2_xy)
d1_7=[]
date7=[]
d2_7=[]

plt.plot(range(1,len(d1)+1),d1, label='Line1_In_current')
plt.plot(range(1,len(d2)+1),d2, label='Line1_Leave_current')

plt.plot(date7,d1_7,'o')
plt.plot(date7,d2_7,'o')
plt.xlabel("日期")
plt.ylabel("当日人流量")



#x轴标记
xzhou=np.arange(1,30,1)
plt.xticks(xzhou)

plt.axis(ymin=5000)



a = [i for i in range(len(d1)) if i % 7 == 5 or i % 7 == 0]
b=  [i for i in range(20000) if i % 2500 ==0]


for i in b:
    plt.hlines(i,xmin=0,xmax=40)
for i in range(1,30):
    plt.plot(i,d1[i-1],'s',color='Blue')


# plt.legend()
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.show()
