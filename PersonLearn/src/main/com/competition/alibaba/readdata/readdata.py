#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/19 下午7:53
# @Author  : niuliangtao
# @Site    : 
# @File    : readdata.py
# @Software: PyCharm


import string
import numpy as np
import matplotlib.pyplot as plt



fileRoot = '/Users/weidian/data/private/'
file1 = fileRoot + "训练数据-ccf_first_round_shop_info.csv"
file2 = fileRoot + "训练数据-ccf_first_round_user_shop_behavior.csv"
file3 = fileRoot + "AB榜测试集-evaluation_public.csv"


# Field   Type    Description Note
# shop_id String  店铺ID    已脱敏
# category_id String  店铺类型ID  共40种左右类型，已脱敏
# longitude   Double  店铺位置-经度 已脱敏，但相对距离依然可信
# latitude    Double  店铺位置-纬度 已脱敏，但相对距离依然可信
# price   Bigint  人均消费指数  从人均消费额脱敏而来，越高表示本店的人均消费额越高
# mall_id String  店铺所在商场ID    已脱敏

def analyseShopInfo():
    fo = open(file1)

    longitude = []
    latitude = []
    fo.readline()
    for i in range(0,10000):
        line = fo.readline()
        if not line:
            break
        strs = line.split(",")

        longitude.append(string.atof(strs[2]))
        latitude.append(string.atof(strs[3]))
    fo.close()

    print len(longitude)

    lx = np.array(longitude)
    ly = np.array(latitude)

    plt.plot(lx, ly, 'o')
    plt.show()


def analyseShopBuy():
    fo = open(file2)

    fo.readline()
    for i in range(0,100):
        line = fo.readline()
        if not line:
            break
        strs = line.split(",")
        print line
    fo.close()



if __name__ == '__main__':
    # analyseShopInfo()
    analyseShopBuy()

