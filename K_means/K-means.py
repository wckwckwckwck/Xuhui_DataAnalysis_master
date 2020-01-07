# 输入:x[1],x[2],x[3],...,x[n],其中每个x[i]都是m维的向量，给定聚类的数目k
# 1.随机生成k个代表元:z[1],z[2],...,z[k];每个z[i]都是第i类的中心元
# 2.repeat:
#   更新 xi所述的类别ci,使得：|x[i]-z[ci]|最小
#   更新 z[j],z[j]等于所在类别G[j]的所有样本的平均值
# until:z不再改变
# '''

#输出颜色聚合后图
import numpy as np
import math
import random
from PIL import Image

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
    filename = 'test_3.jpg'
    im = Image.open(filename).resize((128, 128))

    img = im.load()

    im.close()
    height = im.size[0]
    width = im.size[1]

    X = []
    for i in range(0, height):
        for j in range(0, width):
            X.append(np.array(img[i, j]))

   # 输出数据化的图像，不需要先注释
    for i in range(0, height):
        print("line" + str(i))
        for j in range(0, width):
            print(X[i*width+j],end=' ')
        print( )

    Z, c, k = k_mean(X, k1)
    print(Z)
    new_im = Image.new("RGB", (height, width))
    for i in range(0, height):
        for j in range(0, width):
            index = i * width + j
            pix = list(Z[c[index]])
            for k in range(len(pix)):
                pix[k] = int(pix[k])
            new_im.putpixel((i, j), tuple(pix))

    # new_im.show()
    new_im.save(filepath)


if __name__ == '__main__':
    i1 = 1
    for i1 in range(1,2, 1):
        str2 = "D:\workspace\PythonOutput\RGB_output\对比图\k_means\\test_3\\" + str(i1) + ".jpg"
        test_rgb_img(i1, str2)
    print(cnt)
