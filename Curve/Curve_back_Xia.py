from PIL import Image, ImageDraw
from webcolors import rgb_to_hex, hex_to_rgb
import os

def get_colors(infile, outline_color, outline_width=10, palette_length_div=10, numcolors=10):
    original_image = Image.open(infile)
    image = Image.open(infile)
    small_image = image.resize((80, 80))
    result = small_image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)   # image with only 10 dominating colors
    result.putalpha(0)
    colors = result.getcolors(80*80)      # array of colors in the image
    swatchsize2 = 100

    width, height = original_image.size
    palette_height = int(height/palette_length_div)
    background = Image.new("RGB", (width, height + palette_height))   # blank canvas(original image + palette)
    pal = Image.new("RGB", (width, palette_height))
    pal2 = Image.new("RGB", (numcolors*swatchsize2, swatchsize2))
    draw = ImageDraw.Draw(pal)
    draw2 = ImageDraw.Draw(pal2)
    posx = 0
    posx2 = 0
    swatchsize = width/10
    hex_codes = []

    # making the palette
    for count, col in colors:
        draw.rectangle([posx, 0, posx + swatchsize, palette_height], fill=col, width=outline_width, outline=outline_color)
        draw2.rectangle([posx2, 0, posx2+swatchsize2, swatchsize2], fill=col)
        posx = posx + swatchsize
        posx2 = posx2 + swatchsize2
        hex_codes.append(rgb_to_hex(col[:3]))

    del draw
    del draw2
    box = (0, height, width, height + palette_height)

    # pasting image and palette on the canvas
    background.paste(original_image)
    background.paste(pal, box)
    return background, pal2, hex_codes


if __name__ == '__main__':

    rootdir = 'F:\学校文件\大三\大三上\项目\伦敦、东京、曼哈顿、下城区\伦敦、东京、曼哈顿、下城区\纽约、伦敦\曼哈顿'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            i_str = str(i)
            str2 = 'output_withbackgroud' + i_str + 'e'
            str3= 'output_no_background' + i_str+ 'e'
            background,pal2, hex_codes = get_colors(path, outline_color=hex_to_rgb('#FFFFFF'))
            background.save("D:\workspace\PythonOutput\photo_1\photo_man\ " + str2 + ".jpg")
            pal2.save("D:\workspace\PythonOutput\photo_1\photo_man\ "+str3+".jpg")


    # background, pal2, hex_codes = get_colors('test.jpg', outline_color=hex_to_rgb('#FFFFFF'))
    # background.show()
    # pal2.show()
    # print(hex_codes)
