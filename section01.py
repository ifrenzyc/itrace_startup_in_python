# -*- coding:utf-8 -*-

import os
import pandas as pd
import numpy as np

## df = pd.read_csv('E:/c04-报销/省公司劳动知识竞赛/选拔赛/service.txt',sep = '|',encoding = 'utf-8')

trainFile = "/Users/yangc/src/2017_itrace/itrace_startup_in_python/service.txt"
pwd = os.getcwd()  # 查看当前工作目录
os.chdir(os.path.dirname(trainFile))  # 修改当前工作目录

td = pd.read_csv(os.path.basename(trainFile), sep='|', header=None
                 , names=["uuid", "ser_name", "cust_begin", "serv_begin", "serv_end", "cust_end", "for_time", "back_time"])

os.chdir(pwd)
td.head()

grouped = td.groupby(['ser_name'])
gm = grouped.aggregate({'for_time': np.mean})
print(gm.sort_values(by=['for_time'], ascending=[False]).head())

td['diff'] = td['back_time'] - td['for_time']

std = td.sort_values(by=['diff'], ascending=[False])

print(std[['ser_name', 'diff']].head())
