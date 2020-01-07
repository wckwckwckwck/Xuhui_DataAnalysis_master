from folium import plugins
import folium
import os
import webbrowser
# import bike_data.data_takeline
import pandas as pd
import numpy as np
import xlrd
import math

def RGB_to_HEX(input1, input2, input3):
    str1 = hex(input1)
    str2 = hex(input2)
    str3 = hex(input3)

    str1 = str1[2:]
    str2 = str2[2:]
    str3 = str3[2:]
    str4 = '#' + str(str1 + str2 + str3)
    # while len(str4)<7:
    #     str4+='0'

    return str4


posi = pd.read_excel("来源去向分析.xlsx")
sheet1 = pd.read_excel("来源去向分析.xlsx", sheet_name="去向地")
num = [i for i in range(0, 64) if i % 2 == 0]

loc_s = []
for i in num:
    loc_s.append([sheet1['lat'][i], sheet1['lon'][i]])

cu_s = []
total_s = []
for i in num:
    cu_s.append(sheet1['cu_num'][i])
    total_s.append(sheet1['total_num'][i])



loc = []
shanghai_loc = [31.2303700000, 121.4737000000]
# ”OpenStreetMap”
#
#                 ”Stamen Terrain”, “Stamen Toner”, “Stamen Watercolor”
#
#                 ”CartoDB positron”, “CartoDB dark_matter”
#
#                 ”Mapbox Bright”, “Mapbox Control Room” (Limited zoom)
#
#                 ”Cloudmade” (Must pass API key)
#
#                 ”Mapbox” (Must pass API key)


m = folium.Map([31.208018, 121.498321], zoom_start=10, tiles="Stamen Toner")  # 中心区域的确定
m_total = folium.Map([31.208018, 121.498321], zoom_start=10, tiles="Stamen Toner")  # 中心区域的确定
cu_max = 30444
total_max = 40431
print(cu_s)
for i in range(len(loc_s)):
    loc.clear()
    loc.append(shanghai_loc)
    loc.append(loc_s[i])
    gew=(loc_s[i][0],loc_s[i][1])

    cor_b = 191 + int(31 * cu_s[i] / 30444)
    cor_r = 64 + int(64 * cu_s[i] / 30444)
    cor_g = 123 + int(47 * cu_s[i] / 30444)

       # print(cu_s[i])
    str_m = RGB_to_HEX(cor_r, cor_g, cor_b)
    wid = 3+ 3 * (cu_s[i] / 30444)

    route = folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
        loc,  # 将坐标点连接起来
        weight=wid,  # 线的大小为3
        color=str_m,  # 线的颜色为渐变色
        opacity=1  # 线的透明度
    ).add_to(m)  # 将这条线添加到刚才的区域m内

    circles = folium.Circle(  # polyline方法为将坐标用线段形式连接起来
        gew,  # 将坐标点连接起来
          # 线的大小为3
        color=str_m,  # 线的颜色为渐变色
        opacity=1,
        radius=(800+800*(cu_s[i]/30444)),
        popup=True,
        # 线的透明度
    ).add_to(m)  # 将这条线添加到刚才的区域m内
#绘制目前数据






for i in range(len(loc_s)):
    loc.clear()
    loc.append(shanghai_loc)
    loc.append(loc_s[i])

    cor_b = 191 + int(31 * total_s[i] / 30444)
    cor_r = 64 + int(64 * total_s[i] / 30444)
    cor_g = 123 + int(47 * total_s[i] / 30444)
    str_m = RGB_to_HEX(cor_r, cor_g, cor_b)
    wid = 3 + 3 * (total_s[i] / 30444)
    gew = (loc_s[i][0], loc_s[i][1])
    if (cor_b + cor_g + cor_r > (191 + 64 + 123 + 50)):
        print(total_s[i])
    route = folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
        loc,  # 将坐标点连接起来
        weight=wid,  # 线的大小为3
        color=str_m,  # 线的颜色为渐变色
        opacity=1  # 线的透明度
    ).add_to(m_total)  # 将这条线添加到刚才的区域m内
    circles = folium.Circle(  # polyline方法为将坐标用线段形式连接起来
        gew,  # 将坐标点连接起来
        # 线的大小为3
        color=str_m,  # 线的颜色为渐变色
        opacity=1,
        radius=(800 + 1800 * (cu_s[i] / 30444)),
        popup=True,
        # 线的透明度
    ).add_to(m_total)  # 将这条线添加到刚才的区域m内




# for i in range(len(location_s)):
#     folium.Circle(radius=5, location=location_s[i]).add_to(m)
# m.save(os.path.join(r'C:\Users\Desktop', 'Heatmap1.html'))
m.save('D:\workspace\PythonOutput\\pop_line.html')
webbrowser.open('D:\workspace\PythonOutput\\pop_line.html')
m_total.save('D:\workspace\PythonOutput\\pop_line_total.html')
webbrowser.open('D:\workspace\PythonOutput\\pop_line_total.html')
print(loc_s)
