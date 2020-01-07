import PIL as plt
import random
from PIL import Image
import numpy as np


def random_keans():
    x = []
    y = []
    for i in range(200):
        x.append(random.randint(0, 255))
        y.append(random.randint(0, 255))
    new_image = Image.new(mode='RGB', size=(256, 256), color='White')
    for i in range(199):
        new_image.putpixel(xy=(x[i], y[i]), value=(0, 0, 0))
        # new_image.putpixel((4,4),(255,0,0))
    new_image.show()


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


if __name__ == '__main__':
    random_keans()
