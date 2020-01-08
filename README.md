# Xuhui_DataAnalysis_Master 

目录

 ##### 1.[bike_data](#1) 
 ##### 2.[constucter_edge](#) 
 ##### 3.[Curve](#) 
 ##### 4.[k_mean](#) 
 ##### 5.[plot_3d](#) 


[link1](#j1)

<h2 id="1">1.BikeData-摩拜单车数据</h2>
<h3>核心函数:</h3>

```python
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
```


<h2>2.建筑物轮廓抽取</h2>
<h3>核心函数:opencv_霍夫变换</h3>


```python 
img=cv2.resize(img,(512,512),interpolation =  cv2.INTER_NEAREST)
house = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 获取灰度图
edges = cv2.Canny(house, 50, 200)
lines = cv2.HoughLines(edges, 1, np.pi/180, 260)  # 霍夫变换返回的就是极坐标系中的两个参数  rho和theta
print(np.shape(lines))

```







# j1