

import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import folium



posi=pd.read_excel("宜山路进出站客流_201905.xlsx")

sheet2=pd.read_excel("宜山路进出站客流_201905.xlsx",sheet_name='四号线',skiprows = [0,1])
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
plt.title = '宜山路'
plt.plot(d1, label='Line4_In_current')
plt.plot(d2, label='Line4_Leave_current')
a = [i for i in range(len(d1)) if i % 7 == 5 or i % 7 == 0]
for i in a:
    plt.axvline(i)

# plt.legend()
plt.show()
