#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/06 16:55
# @Author  : niuliangtao
# @Site    : 
# @File    : Test.py
# @Software: PyCharm



import numpy as np
import tensorflow as tf
from tensorflow.python.ops import random_ops

noise_shape = np.array([1, 3])
data1 = np.array([2, 3])
random_tensor = random_ops.random_uniform(noise_shape, dtype=data1)

sess = tf.Session()
# tf.initialize_all_variables() no long valid from
# 2017-03-02 if using tensorflow >= 0.12
sess.run(tf.global_variables_initializer())

print (sess.run(random_tensor))

from tensorflow.python.ops import random_ops

noise_shape = tf.Variable
random_tensor = random_ops.random_uniform(noise_shape,
                                          seed=seed,
                                          dtype=x.dtype)
