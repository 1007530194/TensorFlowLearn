#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/02 21:06
# @Author  : niuliangtao
# @Site    : 
# @File    : DataSet.py
# @Software: PyCharm

from __future__ import print_function

fileRoot = '/Users/weidian/workspace/pycharm/TensorFlowLearn/data/competition1/origin/'
trainPath = fileRoot + "[new] yancheng_train_20171226.csv"
testPath = fileRoot + "yancheng_testA_20171225.csv"


def data():
    """
    1  sale_date       销售日期   201201
    2  class_id        车型ID    234567
    3  sale_quantity   销量      15
    4  brand_id        品牌ID    234
    5  compartment     厢数      3
    6  type_id         车型类别ID  1
    7  level_id        车型级别ID  1
    8  department_id   车型系别ID  1
    9  TR              变速器档位   6
    10 gearbox_type    变速器形式   AT
    11 displacement    排量        2.5
    12 if_charging     是否增压     L
    13 price_level     成交段     35-50W（“W”：万元，“WL”：万元以下）
    14 driven_type_id  驱动形式ID  1
    15 fuel_type_id    燃料种类ID  1
    16 newenergy_type_id   新能源类型ID 1
    17 emission_standards_id   排放标准ID  1
    18 if_MPV_id       是否微客MPV 1
    19 if_luxurious_id 是否豪华ID  1
    20 power           功率  160
    21 cylinder_number 缸数  6
    22 engine_torque   发动机扭矩   250
    23 car_length      车长  4531
    24 car_width       车宽  1817
    25 car_height      车高  1421
    26 total_quality   总质量 1980
    27 equipment_quality 整备质量   1565
    28 rated_passenger 额定载客    5
    29 wheelbase       轴距      2760
    30 front_track     前轮距     1500
    31 rear_track      后轮距     1529
    :return:
    """
    fo = open(trainPath)

    dateMap = {}
    fo.readline()
    total = 0
    for i in range(0,100000):
        line = fo.readline()
        if not line:
            break
        strs = line.split(",")
        dateMap[strs[0]] = dateMap.get(strs[0],0)+1
        total = total + 1
    fo.close()

    print('taotal:' + str(total))
    for key in dateMap.keys():
        print (key + '\t' + str(dateMap.get(key)))


if __name__ == '__main__':
    data()
    import pandas as pd  # 加载模块

    #set low_memory = False
    # 读取csv
    data = pd.read_csv(trainPath, low_memory=False)

    # 打印出data
    print(data.head(5))
    print (data['price'])

