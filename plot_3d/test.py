# 方法一，利用关键字
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import numpy as np
import math
import random
from PIL import Image

address_1 = "D:\\workspace\\PythonOutput\\RGB_output\\对比图\\7.jpg"
cnt = 0


def calculate_zi(Gi, X):
    # 给定Gi,里面包含着属于这个类别的元素，然后计算这些元素的中心点
    # 在本实例中,Gi里面包含的是下标
    global cnt
    sumi = np.zeros(len(X[0]))
    for each in Gi:
        cnt += 1
        sumi += X[each]
    sumi /= (len(Gi) + 0.000000001)
    zi = sumi
    return zi


def find_ci(xi, Z):
    # 寻找离xi最近的中心元素ci,使得Z[ci]与xi之间的向量差的內积最小
    global cnt
    dis_ = np.inf
    len_ = len(Z)
    rst_index = None
    for i in range(len_):
        cnt += 1
        tmp_dist = np.dot(xi - Z[i], np.transpose(xi - Z[i]))  # 将三维向量与自己转置相乘
        if tmp_dist < dis_:
            rst_index = i
            dis_ = tmp_dist
    return rst_index  # 返回理z最近的x的点的编号


def k_mean(X, k):
    G = []  # G[i]={1,2,3...}表示属于第i类的样本在X中的索引，洗标
    Z = []  # Z[i] 第i类的中心点
    N = len(X)
    c = []  # c[i]=1,2,...,k；表示第i个样本属于第c[i]类
    tmpr = set()
    while len(Z) < k:
        r = random.randint(0, len(X) - 1)
        if r not in tmpr:
            tmpr.add(r)
            Z.append(X[r])
            G.append(set())
    for i in range(N):
        c.append(0)
    # 随机生成K个中心元素
    while True:
        group_flag = np.zeros(k)
        for i in range(N):
            new_ci = find_ci(X[i], Z)  # find函数去查找z中离xi距离最近的函数
            if c[i] != new_ci:
                # 找到了更好的,把xi从原来的c[i]调到new_ci去，于是有两个组需要更新：new_ci,c[i]
                if i in G[c[i]]:
                    G[c[i]].remove(i)
                group_flag[c[i]] = 1  # 把i从原来所属的组中移出来
                G[new_ci].add(i)
                group_flag[new_ci] = 1  # 把i加入到新的所属组去
                c[i] = new_ci

        # 上面已经更新好了各元素的所属
        if np.sum(group_flag) == 0:
            # 没有组被修改
            break
        for i in range(k):
            if group_flag[i] == 0:
                # 未修改,无须重新计算
                continue
            else:
                Z[i] = calculate_zi(list(G[i]), X)
    return Z, c, k


def test_rgb_img(k1, filepath):
    filename = 'test_1.jpg'
    im = Image.open(filename).resize((128, 128))
    img = im.load()
    im.close()
    height = im.size[0]
    width = im.size[1]
    X = []
    for i in range(0, height):
        for j in range(0, width):
            X.append(np.array(img[i, j]))
    Z, c, k = k_mean(X, k1)
    print(Z)
    new_im = Image.new("RGB", (height, width))
    for i in range(0, height):
        for j in range(0, width):
            index = i * width + j
            pix = list(Z[c[index]])
            for k in range(len(pix)):
                pix[k] = int(pix[k])
            new_im.putpixel((i,), tuple(pix))

    # new_im.show()
    new_im.save(filepath)
    return Z


# 定义坐标轴
def draw_3d_fromfile(infile):
    filename = infile
    im = Image.open(filename).resize((50, 50))
    img = im.load()
    im.close()
    X = []
    height = im.size[0]
    width = im.size[1]
    for i in range(0, height):
        for j in range(0, width):
            X.append(np.array(img[i, j]))
    xd = []
    yd = []
    zd = []
    for node in X:
        xd.append(node[0])
        yd.append(node[1])
        zd.append(node[2])
    img_re = drwa_3d(xd, yd, zd)
    return img_re


# coding:utf-8

def RGB_to_HEX(input1, input2, input3):
    str1 = hex(input1)
    str2 = hex(input2)
    str3 = hex(input3)

    str1 = str1[2:]
    str2 = str2[2:]
    str3 = str3[2:]
    str4 = '#' + str(str1 + str2 + str3)
    # while len(str4)<7:
    #     str4+='0'

    return str4


def drwa_3d(x, y, z):
    fig = plt.figure()
    ax1 = plt.axes(projection='3d')
    # ax = fig.add_subplot(111,projection='3d')  #这种方法也可以画多个子图
    # 定义图像和三维格式坐标轴
    # fig = plt.figure()
    # ax2 = Axes3D(fig)
    # z = np.linspace(0, 13, 1000)
    # x = 5 * np.sin(z)
    # y = 5 * np.cos(z)
    # zd = 13 * np.random.random(100)
    # xd = 5 * np.sin(zd)
    # yd = 5 * np.cos(zd)

    # ax1.scatter3D(x, y, z ,cmap='Black',edgecolors='#000000')
    for i in range(len(x)):
        co = RGB_to_HEX(x[i], y[i], z[i])
        if(len(co)<7):
            continue
        co = co.upper()
        ax1.scatter3D(x[i], y[i], z[i], c=co)
    # 绘制散点图
    # ax1.plot3D(x, y, z, 'pink')  # 绘制空间曲线

    plt.show()
    plt.angle_spectrum
    return ax1


if __name__ == '__main__':

    img_1 = draw_3d_fromfile('12.jpg')


    # img_1.save("D:\\workspace\\PythonOutput\\3D_RGBlayout\\1.jpg")
    # img_2=draw_3d_fromfile('2.jpg')
    # img_3=draw_3d_fromfile('4.jpg')
    # img_7=draw_3d_fromfile('7.jpg')
