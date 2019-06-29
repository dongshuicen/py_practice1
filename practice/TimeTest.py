# -*- coding: utf-8 -*-
import time

print(time.localtime(time.time()))
print("格式化后当前日期：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
import calendar

months = {1,2,3,4,5,6,7,8,9,10,11,12}
years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
for y in years:
    for i in months:
        print(calendar.month(y, i))
