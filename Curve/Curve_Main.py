import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import folium


def draw_curse(filepath="上海体育馆进出站客流_201905.xlsx", day_n=31, sheetname='一号线',ymin_tmp=5000,ymax_tmp=20000):
    posi = pd.read_excel(filepath)
    sheet2 = pd.read_excel(filepath, sheet_name=sheetname, skiprows=[0, 1])
    data1 = sheet2.iloc[21].values
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
    # 输出数组
    print(d1)
    print(d2)

    plt.title = '上海体育馆'
    d1_xy = []
    d2_xy = []
    for i in range(1, day_n):
        d1_xy.append((i, d1[i-1]))
        d2_xy.append((i, d2[i-1]))

    d1_7 = []
    date7 = []
    d2_7 = []
    # 画线
    plt.plot(range(1, len(d1) + 1), d1, label=sheetname+"入人流量", color='#C3E199')
    plt.plot(range(1, len(d2) + 1), d2, label=sheetname+"出人流量", color='#FFF0AB')

    a = [i for i in range(len(d1)) if i % 7 == 5 or i % 7 == 0]
    b = [i for i in range(ymin_tmp,ymax_tmp) if i % 2500 == 0]
    # 画标记线
    for i in b:
        plt.hlines(i, xmin=0, xmax=32)

        # 画点
    for i in range(1, day_n+1):
        plt.plot(i, d1[i - 1], 's', color='#C3E199')
        plt.plot(i, d2[i - 1], 's', color="#FFF0AB")

    zhoumo = []
    zhoumo_d = []
    for i in range(1, day_n+1):
        if i % 7 == 6 or i % 7 == 0:
            zhoumo.append(i)
            zhoumo_d.append(d1[i - 1])

    # 画周末点
    zhoumo_1 = [6, 7]
    zhoumo_2 = [13, 14]
    zhoumo_3 = [20, 21]
    zhoumo_4 = [27, 28]
    zhoumo_1_d = [d1[5], d1[6]]
    zhoumo_2_d = [d1[12], d1[13]]
    zhoumo_3_d = [d1[19], d1[20]]
    zhoumo_4_d = [d1[26], d1[27]]
    plt.plot(zhoumo_1, zhoumo_1_d, color='#A2D4C8')
    plt.plot(zhoumo_1, zhoumo_1_d, 's', color='#A2D4C8')
    plt.plot(zhoumo_2, zhoumo_2_d, color='#A2D4C8')
    plt.plot(zhoumo_2, zhoumo_2_d, 's', color='#A2D4C8')
    plt.plot(zhoumo_3, zhoumo_3_d, color='#A2D4C8')
    plt.plot(zhoumo_3, zhoumo_3_d, 's', color='#A2D4C8')
    plt.plot(zhoumo_4, zhoumo_4_d, color='#A2D4C8')
    plt.plot(zhoumo_4, zhoumo_4_d, 's', color='#A2D4C8')

    zhoumo_1_d_2 = [d2[5], d2[6]]
    zhoumo_2_d_2 = [d2[12], d2[13]]
    zhoumo_3_d_2 = [d2[19], d2[20]]
    zhoumo_4_d_2 = [d2[26], d2[27]]
    plt.plot(zhoumo_1, zhoumo_1_d_2, color='#FFA200')
    plt.plot(zhoumo_1, zhoumo_1_d_2, 's', color='#FFA200')
    plt.plot(zhoumo_2, zhoumo_2_d_2, color='#FFA200')
    plt.plot(zhoumo_2, zhoumo_2_d_2, 's', color='#FFA200')
    plt.plot(zhoumo_3, zhoumo_3_d_2, color='#FFA200')
    plt.plot(zhoumo_3, zhoumo_3_d_2, 's', color='#FFA200')
    plt.plot(zhoumo_4, zhoumo_4_d_2, color='#FFA200')
    plt.plot(zhoumo_4, zhoumo_4_d_2, 's', color='#FFA200')

    plt.plot(date7, d1_7, 'o')
    plt.plot(date7, d2_7, 'o')

    plt.xlabel('                                                                                              日期')
    plt.ylabel("                                         当日人流量")

    # x轴标记
    xzhou = np.arange(1, day_n+1, 1)
    plt.xticks(xzhou)
#设置曲线底线
    plt.axis(ymin=ymin_tmp, xmax=40)

    plt.legend(loc='right')
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.show()



if __name__ == '__main__':
    xu_name="徐家汇进出站客流_201905.xlsx"
    ti_name="上海体育馆进出站客流_201905.xlsx"
    draw_curse(filepath="上海体育馆进出站客流_201905.xlsx",sheetname="四号线",ymin_tmp=5000,ymax_tmp=25000)
