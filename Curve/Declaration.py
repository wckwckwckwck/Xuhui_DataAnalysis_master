from PIL import Image, ImageDraw
from webcolors import rgb_to_hex, hex_to_rgb


def get_colors(infile, outline_color, outline_width=10, palette_length_div=10, numcolors=10):
    #定义调用函数：变量infile：输入文件numcolor表示提取颜色数量，默认为10
    original_image = Image.open(infile)
    image = Image.open(infile)      #读取文件，生成image对象
    small_image = image.resize((80, 80))   #将文件缩略成80*80的缩略图

    result = small_image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)   # 调用image类下的convert函数，'p'表示调色板模式
    #palette表示调色板为image自适应模式，colorr调用numcolors=10
    #输出为采用十个出现最频繁的颜色拟合成的原图片

    #关于convert函数：
    # def convert(self, mode=None, matrix=None, dither=None,
    #             palette=WEB, colors=256): #输入参数：self为图像自身，mode函数处理模式，martrix，dither默认均为零，
    #   pallette表示调色板模式，输入使用ADPTIVE自适应模式，colors表示需要提取的颜色数目
    #已去除无关部分——————————————
    #
    #     if mode == "P" and palette == ADAPTIVE:   #判断输入模式是否为调色板模式，调色板设置是否为自适应模式
    #
    #         im = self.im.quantize(colors)        #调用ImagingCore类下的quantize方法


#quantize方法：
  #k-means图像聚类算法















    #         new = self._new(im)      #得到新加工后的im对象后，用Image构建方法产生新的图片
    #         return new      #返回得到的图片
    #convert函数结束————————————————————————
    #






    # colors = result.getcolors(10)      # 开数组存储图片中的颜色，
    # swatchsize2 = 100
    #
    # width, height = original_image.size
    # palette_height = int(height/palette_length_div)
    # background = Image.new("RGB", (width, height + palette_height))   # 保留原图片，以RGB图片格式保留长款输出
    #
    # posx = 0
    # posx2 = 0
    # swatchsize = width/10
    # hex_codes = []
    #
    # # making the palette
    # for count, col in colors:
    #     draw.rectangle([posx, 0, posx + swatchsize, palette_height], fill=col, width=outline_width, outline=outline_color)
    #     draw2.rectangle([posx2, 0, posx2+swatchsize2, swatchsize2], fill=col)
    #     posx = posx + swatchsize
    #     posx2 = posx2 + swatchsize2
    #     hex_codes.append(rgb_to_hex(col[:3]))
    #
    # #将colors中颜色输出，每个占据十分之一的长宽
    #
    #
    #
    #


if __name__ == '__main__':

    background, pal2, hex_codes = get_colors('test.jpg', outline_color=hex_to_rgb('#FFFFFF'))  #主函数参数：输入图片，输出图片按照RGB的十六进制输出
    background.show()
    pal2.show()
    print(hex_codes)