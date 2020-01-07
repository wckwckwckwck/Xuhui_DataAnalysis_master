import shapely, geopandas, fiona
import seaborn as sns
from fiona.crs import from_epsg, from_string

tpath = 'sheshi.shp '

shp_df = geopandas.GeoDataFrame.from_file(tpath, encoding='gb18030')
shp_df.head()  # 获取表头
shp_df.plot()

print(shp_df.head())