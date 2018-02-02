#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/01/29 16:57
# @Author  : niuliangtao
# @Site    : 
# @File    : Test.py
# @Software: PyCharm


#!/usr/bin/python
# -*- coding: UTF-8 -*-

def reserve(list):
    i = 0;
    a = 0;
    j = len(list)-1;
    while i <= (len(list)-1)/2:
        print i
        print j
        a = list[i];
        list[i] = list[j];
        list[j] = c;
        i = i+1;
        j = j-1;
    return [list]

List = raw_input("输入任意一维数组:");
print"Received input is:",List
reserve(List);
print List
