import re
import bike_data.time_change
import bike_data.draw_map
f = open("F:\\学校文件\大三\大三上\项目\\2019上海城市设计挑战赛\摩拜骑行数据\\text_1.txt", "r")
str = f.readline()
str = re.split('[,#;]', str) #串分割后每三个一组，
lat=[]
y = []
for i in range(0, len(str)):
    if i % 3 == 0:
        x = []
        x.append(str[i])
        x.append(str[i + 1])
        s1=float(str[i])
        s2=float(str[i+1])
        lat.append([s1 ,s2])
        data1 = int(str[i + 2])
        data1 = int(data1/1000)
        # data1= str(data1)
        data1 = bike_data.time_change.time_change_f(data1)
        #data1为时间戳
        x.append(data1)
        y.append(x)

print(str)
print(y)
print(lat)
bike_data.draw_map.draw_map_f(lat)