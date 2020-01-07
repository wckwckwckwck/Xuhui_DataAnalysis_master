import xlrd
import bike_data
import re
filename = '摩拜骑行数据.xlsx'

def drawfromstring(strinput):
    str_return = re.split('[,#;]', strinput) #串分割后每三个一组，
    len_s=len(str_return)
    res=(float(str_return[len_s-3]),float(str_return[len_s-2]))

    return res

def extract(inpath="data_pre30.xlsx"):
    data = xlrd.open_workbook(inpath, encoding_override='utf-8')
    table = data.sheets()[0]  # 选定表
    nrows = table.nrows  # 获取行号
    ncols = table.ncols  # 获取列号
    data_end=[]
    for i in range(1, min(10000,nrows)):  # 第0行为表头
        alldata = table.row_values(i)  # 循环输出excel表中每一行，即所有数据
        result =str( alldata[1])  # 取出表中第二列数据
        str_result=drawfromstring(result)
        print(str(i),end=' ')
        print(str_result)
        data_end.append(str_result)
    return data_end

if __name__ == "__main__":
    inpath = 'data_pre30.xlsx'  # excel文件所在路径
    data=extract(inpath)
    print(data)
