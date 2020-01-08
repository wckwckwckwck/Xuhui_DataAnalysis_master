import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image
cap = cv2.VideoCapture(0)
# rgb颜色转化为对应的hsv颜色
if not cap.isOpened():
    print('摄像头打开失败')
else:
    print('摄像头打开成功')


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


# lower_red=np.array([0,43,46])
# upper_red=np.array([15,255,255])
lower_red = np.array(rgb2hsv(146, 128, 128), dtype=np.int32)

upper_red = np.array(rgb2hsv(127, 133, 156), dtype=np.int32)
while (1):

    im = Image.open("12.jpg").resize((50, 50))
    img = im.load()
    frame = cv2.imread('12.jpg',1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 根据阈值构建掩模
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # 对图像和掩模进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('iframe', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    # k = cv2.waitKey(1) & 0xFF
    # if k == 27:
    #     break
    #     cv2.destroyAllWindows()