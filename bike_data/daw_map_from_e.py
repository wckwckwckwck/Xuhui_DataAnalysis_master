import xlwt

sheet2=pd.read_excel("宜山路进出站客流_201905.xlsx",sheet_name='四号线',skiprows = [0,1])
data1=sheet2.iloc[21].values
data2 = sheet2.iloc[21].values