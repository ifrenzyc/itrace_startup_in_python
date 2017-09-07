# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from pandas import DataFrame

column_names = ["uuid", "serv_name", "cust_begin", "serv_begin", "serv_end", "cust_end", "cust_time", "serv_time"]
df = DataFrame(pd.read_table("service.txt", sep="|", header=None, names=column_names))

grouped = df.groupby("serv_name")
grouped_mean = grouped.aggregate({"cust_time": np.mean})
sortedCustTime = grouped_mean.sort_values(by="cust_time", ascending=False)
print sortedCustTime.head(n=5)
# ["cust_time"].mean()
# dfg.columns = ["serv_name", "cust_time_avg"]
# print(dfg.sort_values().head(n=5))

df["cost"] = df["serv_time"] - df["cust_time"]
cost_df = df.sort_values(by="cost", ascending=False)
print cost_df[["serv_name", "cost"]].head(n=5)
