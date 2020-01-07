from folium import plugins
import folium
import os
import webbrowser
# import bike_data.data_takeline
import pandas as pd
import numpy as np
import xlrd


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
wid=3

# route = folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
#     loc,  # 将坐标点连接起来
#     weight=wid,  # 线的大小为3
#     color='Blue',  # 线的颜色为渐变色
#     opacity=1  # 线的透明度
# ).add_to(m)  # 将这条线添加到刚才的区域m内

circles = folium.Circle(  # polyline方法为将坐标用线段形式连接起来
    (31.208018, 121.498321), # 将坐标点连接起来
      # 线的大小为3
    color='Blue',  # 线的颜色为渐变色
    opacity=1,
    radius=1600,
    popup='popup',
    # 线的透明度
).add_to(m)  # 将这条线添加到刚才的区域m内
#绘制目前数据






# for i in range(len(location_s)):
#     folium.Circle(radius=5, location=location_s[i]).add_to(m)
# m.save(os.path.join(r'C:\Users\Desktop', 'Heatmap1.html'))
m.save('1.html')
webbrowser.open('1.html')
