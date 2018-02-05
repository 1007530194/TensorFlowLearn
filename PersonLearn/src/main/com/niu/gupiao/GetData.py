#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/02/05 16:47
# @Author  : niuliangtao
# @Site    : 
# @File    : GetData.py
# @Software: PyCharm

rawstock=list(DataAPI.MktEqudGet(tradeDate=u"20150513",secID=u"",ticker=u"",beginDate=u"",
                   endDate=u"",isOpen="",field=u"",pandas="1")['secID'])
print rawstock
stocklist=[]
for stock in rawstock:
    s=stock[0:3]
    if s=="600":
        stocklist.append(stock)
    else:
        pass
print stocklist
print len(stocklist)

