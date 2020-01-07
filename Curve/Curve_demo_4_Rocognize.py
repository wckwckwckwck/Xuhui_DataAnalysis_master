
import os
import os.path

from PIL import Image, ImageDraw
from webcolors import rgb_to_hex, hex_to_rgb


def get_colors(infile, outline_color, outline_width=10, palette_length_div=10, numcolors=5):
    image = Image.open(infile)
    small_image = image.resize((256, 256))
    small_image.show()
    result = small_image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)   # image with only 10 dominating colors
    result.putalpha(0)
    colors = result.getcolors(5)      # array of colors in the image
    print(colors)
    swatchsize2 = 100

    pal2 = Image.new("RGB", (numcolors*swatchsize2, swatchsize2))
    draw2 = ImageDraw.Draw(pal2)
    posx2 = 0
    hex_codes = []

    # making the palette
    for count, col in colors:
        draw2.rectangle([posx2, 0, posx2+swatchsize2, swatchsize2], fill=col)
        posx2 = posx2 + swatchsize2
        hex_codes.append(rgb_to_hex(col[:3]))

    del draw2
    return pal2, hex_codes


if __name__ == '__main__':
    pal2, hex_codes = get_colors('test.jpg', outline_color=hex_to_rgb('#FFFFFF'))
    # rootdir = 'F:\学校文件\大三\大三上\项目\伦敦、东京、曼哈顿、下城区\伦敦、东京、曼哈顿、下城区\下东区'
    # list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    # for i in range(0, len(list)):
    #     path = os.path.join(rootdir, list[i])
    #     if os.path.isfile(path):
    #       i_str=str(i)
    #       str2='output'+i_str+'e'
    #       pal2, hex_codes = get_colors(path, outline_color=hex_to_rgb('#FFFFFF'))
    #       pal2.save("D:\workspace\PythonOutput\photo_1\photo_London\ "+str2+".jpg")
    #

