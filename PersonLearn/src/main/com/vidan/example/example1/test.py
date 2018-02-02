#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/11 下午4:06
# @Author  : niuliangtao
# @Site    : 
# @File    : test.py
# @Software: PyCharm


from skimage import io, transform
import glob
import os
import tensorflow as tf
import numpy as np
import time
import pdb

# 将所有的图片resize成100*100
width = 100
height = 100
channel = 3


class Test:

    # 读取图片
    def read_img(self, path):
        # pdb.set_trace()
        cate = [path + x for x in os.listdir(path) if os.path.isdir(path + x)]

        imgs = []
        labels = []
        for idx, folder in enumerate(cate):
            for im in glob.glob(folder + '/*.jpg'):
                print('reading the images:%s' % (im))
                img = io.imread(im)
                img = transform.resize(img, (width, height))
                imgs.append(img)
                labels.append(idx)
        return np.asarray(imgs, np.float32), np.asarray(labels, np.int32)

    # 定义一个函数，按批次取数据
    def minibatches(self, inputs=None, targets=None, batch_size=None, shuffle=False):
        assert len(inputs) == len(targets)
        if shuffle:
            indices = np.arange(len(inputs))
            np.random.shuffle(indices)
        for start_idx in range(0, len(inputs) - batch_size + 1, batch_size):
            if shuffle:
                excerpt = indices[start_idx:start_idx + batch_size]
            else:
                excerpt = slice(start_idx, start_idx + batch_size)
            yield inputs[excerpt], targets[excerpt]

    def train(self, path):
        data, label = self.read_img(path)

        # 打乱顺序
        num_example = data.shape[0]
        arr = np.arange(num_example)
        np.random.shuffle(arr)
        data = data[arr]
        label = label[arr]

        # 将所有数据分为训练集和验证集
        ratio = 0.8
        s = np.int(num_example * ratio)
        x_train = data[:s]
        y_train = label[:s]
        x_val = data[s:]
        y_val = label[s:]

        # -----------------构建网络----------------------
        # 占位符
        x = tf.placeholder(tf.float32, shape=[None, width, height, channel], name='x')
        y_ = tf.placeholder(tf.int32, shape=[None, ], name='y_')

        # 第一个卷积层（100——>50)
        conv1 = tf.layers.conv2d(
            inputs=x,
            filters=32,
            kernel_size=[5, 5],
            padding="same",
            activation=tf.nn.relu,
            kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
        pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)

        # 第二个卷积层(50->25)
        conv2 = tf.layers.conv2d(
            inputs=pool1,
            filters=64,
            kernel_size=[5, 5],
            padding="same",
            activation=tf.nn.relu,
            kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
        pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)

        # 第三个卷积层(25->12)
        conv3 = tf.layers.conv2d(
            inputs=pool2,
            filters=128,
            kernel_size=[3, 3],
            padding="same",
            activation=tf.nn.relu,
            kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
        pool3 = tf.layers.max_pooling2d(inputs=conv3, pool_size=[2, 2], strides=2)

        # 第四个卷积层(12->6)
        conv4 = tf.layers.conv2d(
            inputs=pool3,
            filters=128,
            kernel_size=[3, 3],
            padding="same",
            activation=tf.nn.relu,
            kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
        pool4 = tf.layers.max_pooling2d(inputs=conv4, pool_size=[2, 2], strides=2)

        re1 = tf.reshape(pool4, [-1, 6 * 6 * 128])

        # 全连接层
        dense1 = tf.layers.dense(inputs=re1,
                                 units=1024,
                                 activation=tf.nn.relu,
                                 kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
                                 kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))

        dense2 = tf.layers.dense(inputs=dense1,
                                 units=512,
                                 activation=tf.nn.relu,
                                 kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
                                 kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))

        y_predict = tf.layers.dense(inputs=dense2,
                                 units=5,
                                 activation=None,
                                 kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
                                 kernel_regularizer=tf.contrib.layers.l2_regularizer(0.003))
        # ---------------------------网络结束---------------------------

        loss = tf.losses.sparse_softmax_cross_entropy(labels=y_, logits=y_predict)
        train_op = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

        correct_prediction = tf.equal(tf.cast(tf.argmax(y_predict, 1), tf.int32), y_)
        acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        # 训练和测试数据，可将n_epoch设置更大一些
        n_epoch = 10
        batch_size = 32
        sess = tf.InteractiveSession()
        sess.run(tf.global_variables_initializer())
        for epoch in range(n_epoch):
            start_time = time.time()

            # training
            train_loss, train_acc, n_batch1 = 0, 0, 0
            for x_train_a, y_train_a in self.minibatches(x_train, y_train, batch_size, shuffle=True):
                _, err, ac = sess.run([train_op, loss, acc], feed_dict={x: x_train_a, y_: y_train_a})
                train_loss += err
                train_acc += ac
                n_batch1 += 1

            # validation
            val_loss, val_acc, n_batch2 = 0, 0, 0
            for x_val_a, y_val_a in self.minibatches(x_val, y_val, batch_size, shuffle=False):
                err, ac = sess.run([loss, acc], feed_dict={x: x_val_a, y_: y_val_a})
                val_loss += err
                val_acc += ac
                n_batch2 += 1

            print("\t train loss: %f\t train acc: %f\t validation loss: %f\t validation acc: %f" %
                  (train_loss / n_batch1, train_acc / n_batch1, val_loss / n_batch2, val_acc / n_batch2))

        sess.close()


if __name__ == '__main__':
    path = "../../../data/flower_photos/"
    test1 = Test()
    test1.train(path)
    # data, label = test1.read_img(path)


