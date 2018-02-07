#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/06 18:06
# @Author  : niuliangtao
# @Site    : 
# @File    : one_hot.py
# @Software: PyCharm

import tensorflow as tf

SIZE = 6
CLASS = 8

label1 = tf.constant([1, 3])
b = tf.one_hot(label1, CLASS)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    print('label1:', sess.run(label1))
    print('after one_hot', sess.run(b))

from sklearn import preprocessing

print ('#############################################')
enc = preprocessing.OneHotEncoder()
enc.fit([[2, 0, 3], [1, 1, 0], [1, 2, 1], [10, 0, 2]])

array = enc.transform([[10, 1, 3]]).toarray()

print(array)
