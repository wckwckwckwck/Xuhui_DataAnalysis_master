import re
import bike_data.time_change
import bike_data.draw_map
def drawfromstring(strinput):
    str_return = re.split('[,#;]', strinput) #串分割后每三个一组，
    return str_return

if __name__ == '__main__':
    print(drawfromstring("1;2"))
    #返回值为列表['1', '2']


