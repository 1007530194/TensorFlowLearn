#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 下午4:51
# @Author  : niuliangtao
# @Site    : 
# @File    : DataTF.py
# @Software: PyCharm


import pdb
import numpy as np
import random
import matplotlib.pyplot as plt


def get_train_data(batch_size=32):
    # 生成的数据特征维数为10,lable为前5个维度的特征 * 2 + 后五个维度的特征 * 3得到
    X1, X2 = [], []
    Y1, Y2 = [], []

    for i in range(0, batch_size):
        x1 = []
        x2 = []
        o1 = 0.0
        o2 = 0.0
        for j in range(0, 10):
            r1 = random.random()
            r2 = random.random()
            x1.append(r1)
            x2.append(r2)

            mu = 2.0
            if j >= 5: mu = 3.0
            o1 += r1 * mu
            o2 += r2 * mu
        X1.append(x1)
        Y1.append([o1])
        X2.append(x2)
        Y2.append([o2])

    return (np.array(X1), np.array(X2)), (np.array(Y1), np.array(Y2))


if __name__ == '__main__':
    data = get_train_data()
    print (data[1][1] - data[1][0])
    # pdb.set_trace()

