from folium import plugins
import folium
import os
import webbrowser
import bike_data.data_takeline

def draw_map_f(location_s):
    m = folium.Map([31.208018, 121.498321], zoom_start=10,tiles="Stamen Terrain")  # 中心区域的确定
    # 输入坐标点（注意）folium包要求坐标形式以纬度在前，经度在后
    # route = folium.PolyLine(  # polyline方法为将坐标用线段形式连接起来
    #     location,  # 将坐标点连接起来
    #     weight=10,  # 线的大小为3
    #     color='Green',  # 线的颜色为橙色
    #     opacity=1  # 线的透明度
    # ).add_to(m)  # 将这条线添加到刚才的区域m内
    for i in range(len(location_s)):
        folium.Circle(radius=5, location=location_s[i]).add_to(m)
    # m.save(os.path.join(r'C:\Users\Desktop', 'Heatmap1.html'))
    m.save('D:\workspace\PythonOutput\\bike_data\\heatmap2.html')
    webbrowser.open('D:\workspace\PythonOutput\\bike_data\\heatmap2.html')
# webbrowser.open(file_path2)  # 默认浏览器打开
# 将结果以HTML形式保存到桌面上

if __name__ == "__main__":
    filename="摩拜骑行数据.xlsx"
    loc=bike_data.data_takeline.extract(filename)
    draw_map_f(loc)