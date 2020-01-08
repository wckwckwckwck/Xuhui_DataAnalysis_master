import math

"""
  @:parameter:R<G<B以0-255数值输入
  @:return :返回以E，S，L格式返回
"""
def RGB_TO_HSL_fuc(r, g, b):
    r=r/255
    g=g/255
    b=b/255
    min_t = min(r, g, b)
    max_t = max(r, g, b)
    delta = max_t - min_t
    l = (min_t + max_t) / 2
    l_s=l
    s = 0
    if 0 < l < 1:
        if l < 0.5:
            l = 2 * l
        elif l > 0.5:
            l = 2 * (1 - l)
        s = delta / l
    h = 0
    if delta > 0:
        if (max_t == r and g>b): h += (g - b) / delta
        if (max_t == r and b>=g): h += (6+(g - b) / delta)
        if (max_t == g and max_t != b): h += (2 + (b - r) / delta)
        if (max_t == b and max_t != r): h += (4 + (r - g) / delta)
        h /= 6

    #print(h * 255, s * 255, l_s * 255)
    return (h*255,s*255,l_s*255)



def rgb2hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g - b) / m) * 60
        else:
            h = ((g - b) / m) * 60 + 360
    elif mx == g:
        h = ((b - r) / m) * 60 + 120
    elif mx == b:
        h = ((r - g) / m) * 60 + 240
    if mx == 0:
        s = 0
    else:
        s = m / mx
    v = mx
    H = h / 2
    S = s * 255.0
    V = v * 255.0
    return H, S, V

def hsv_to_loc(h,s,v):
    h=h/360
    s=s/255
    v=v/255
    x0=255/2
    y0=255/2
    z0=0
    r=255/2*s
    x_r=x0+r*math.cos(h)
    y_r=y0+r*math.sin(h)
    z_r=2550/2*v
    return(x_r,y_r,z_r)

if __name__ == "__main__":
    r=247
    g=9
    b=9
    """
       @return： 返回值为H，S，V h（0-360) s(0-255) v(0-255)
    """
    print(rgb2hsv(r,g,b))
