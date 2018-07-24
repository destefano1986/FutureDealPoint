# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

data = pd.read_csv('data.csv', encoding = 'gbk')
data.columns = ['datetime', 'open', 'high', 'low', 'close', 'cjl', 'ccl']

avg = pd.Series()
avg = np.mean(data.loc[20:30, 'close'])
print (avg)