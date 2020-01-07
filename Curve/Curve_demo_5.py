from PIL import Image, ImageDraw
from webcolors import rgb_to_hex, hex_to_rgb


def get_colors(infile, numcolors=10):
    image = Image.open(infile)
    small_image = image.resize((80, 80))
    result = small_image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)   # image with only 10 dominating colors
    result.putalpha(0)
    colors = result.getcolors(80*80)      # array of colors in the image
    hex_codes = []

    # making the palette
    for count, col in colors:
        hex_codes.append(rgb_to_hex(col[:3]))

    return hex_codes


if __name__ == '__main__':
    hex_codes = get_colors('test.jpg')
    print(hex_codes)
