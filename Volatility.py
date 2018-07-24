# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


def read_data():
    global data
    data = pd.read_csv('data_day_coal.csv', encoding = 'gbk')
    data.columns = ['datetime', 'open', 'high', 'low', 'close', 'cjl', 'ccl']

def calc_core(int):
    global data
    global threshold1, threshold2, threshold3, threshold4, threshold5, threshold6, threshold7, threshold8, threshold9, threshold10, threshold12, threshold14, threshold16, threshold18, threshold20, threshold20p
    global thres1, thres2, thres3, thres4, thres5, thres6, thres7, thres8, thres9, thres10, thres12, thres14, thres16, thres18, thres20, thres20p
    global threshold, thres
    for i in range(60, len(data)-60):
        tmp, tmpcc = 0, 0
        for j in range(0, int):
            maximum = (data.loc[i + j + 1, 'high'] - data.loc[i, 'close']) / data.loc[i, 'close']
            if maximum > tmp:
                tmp = maximum
            minimum = (data.loc[i, 'close'] - data.loc[i + j + 1, 'low']) / data.loc[i + j + 1, 'low']
            if minimum > tmpcc:
                tmpcc = minimum
        if tmp <= 0.01 and tmp > 0:
            threshold1 = threshold1 + 1
        elif tmp <= 0.02 and tmp > 0.01:
            threshold2 = threshold2 + 1
        elif tmp <= 0.03 and tmp > 0.02:
            threshold3 = threshold3 + 1
        elif tmp <= 0.04 and tmp > 0.03:
            threshold4 = threshold4 + 1
        elif tmp <= 0.05 and tmp > 0.04:
            threshold5 = threshold5 + 1
        elif tmp <= 0.06 and tmp > 0.05:
            threshold6 = threshold6 + 1
        elif tmp <= 0.07 and tmp > 0.06:
            threshold7 = threshold7 + 1
        elif tmp <= 0.08 and tmp > 0.07:
            threshold8 = threshold8 + 1
        elif tmp <= 0.09 and tmp > 0.08:
            threshold9 = threshold9 + 1
        elif tmp <= 0.1 and tmp > 0.09:
            threshold10 = threshold10 + 1
        elif tmp <= 0.12 and tmp > 0.1:
            threshold12 = threshold12 + 1
        elif tmp <= 0.14 and tmp > 0.12:
            threshold14 = threshold14 + 1
        elif tmp <= 0.16 and tmp > 0.14:
            threshold16 = threshold16 + 1
        elif tmp <= 0.18 and tmp > 0.16:
            threshold18 = threshold18 + 1
        elif tmp <= 0.2 and tmp > 0.18:
            threshold20 = threshold20 + 1
        elif tmp > 0.2:
            threshold20p = threshold20p + 1
        if tmpcc <= 0.01 and tmpcc > 0:
            thres1 = thres1 + 1
        elif tmpcc <= 0.02 and tmpcc > 0.01:
            thres2 = thres2 + 1
        elif tmpcc <= 0.03 and tmpcc > 0.02:
            thres3 = thres3 + 1
        elif tmpcc <= 0.04 and tmpcc > 0.03:
            thres4 = thres4 + 1
        elif tmpcc <= 0.05 and tmpcc > 0.04:
            thres5 = thres5 + 1
        elif tmpcc <= 0.06 and tmpcc > 0.05:
            thres6 = thres6 + 1
        elif tmpcc <= 0.07 and tmpcc > 0.06:
            thres7 = thres7 + 1
        elif tmpcc <= 0.08 and tmpcc > 0.07:
            thres8 = thres8 + 1
        elif tmpcc <= 0.09 and tmpcc > 0.08:
            thres9 = thres9 + 1
        elif tmpcc <= 0.1 and tmpcc > 0.09:
            thres10 = thres10 + 1
        elif tmpcc <= 0.12 and tmpcc > 0.1:
            thres12 = thres12 + 1
        elif tmpcc <= 0.14 and tmpcc > 0.12:
            thres14 = thres14 + 1
        elif tmpcc <= 0.16 and tmpcc > 0.14:
            thres16 = thres16 + 1
        elif tmpcc <= 0.18 and tmpcc > 0.16:
            thres18 = thres18 + 1
        elif tmpcc <= 0.2 and tmpcc > 0.18:
            thres20 = thres20 + 1
        elif tmpcc > 0.2:
            thres20p = thres20p + 1

def threshold_add():
    global threshold1, threshold2, threshold3, threshold4, threshold5, threshold6, threshold7, threshold8, threshold9, threshold10, threshold12, threshold14, threshold16, threshold18, threshold20, threshold20p
    global thres1, thres2, thres3, thres4, thres5, thres6, thres7, thres8, thres9, thres10, thres12, thres14, thres16, thres18, thres20, thres20p
    global threshold, thres
    threshold.append(threshold1)
    threshold.append(threshold2)
    threshold.append(threshold3)
    threshold.append(threshold4)
    threshold.append(threshold5)
    threshold.append(threshold6)
    threshold.append(threshold7)
    threshold.append(threshold8)
    threshold.append(threshold9)
    threshold.append(threshold10)
    threshold.append(threshold12)
    threshold.append(threshold14)
    threshold.append(threshold16)
    threshold.append(threshold18)
    threshold.append(threshold20)
    threshold.append(threshold20p)
    thres.append(thres1)
    thres.append(thres2)
    thres.append(thres3)
    thres.append(thres4)
    thres.append(thres5)
    thres.append(thres6)
    thres.append(thres7)
    thres.append(thres8)
    thres.append(thres9)
    thres.append(thres10)
    thres.append(thres12)
    thres.append(thres14)
    thres.append(thres16)
    thres.append(thres18)
    thres.append(thres20)
    thres.append(thres20p)

def zhisun_calc():
    global threshold, thres
    zssum_up = 0
    for i in range(0, 16):
        zssum_up = zssum_up + threshold[i]
        zsprob_up = zssum_up / sum(threshold)
        print ('zhisun_up probability-' + str(i) + ':' + str(threshold[i]) + '      cdf: ' + '%.3f' % zsprob_up)
    zssum_down = 0
    for i in range(0, 16):
        zssum_down = zssum_down + thres[i]
        zsprob_down = zssum_down / sum(thres)
        print ('zhisun_down probability-' + str(i) + ':' + str(thres[i]) + '      cdf: ' + '%.3f' % zsprob_down)



if __name__ == "__main__":
    threshold1, threshold2, threshold3, threshold4, threshold5, threshold6, threshold7, threshold8, threshold9, \
    threshold10, threshold12, threshold14, threshold16, threshold18, threshold20, threshold20p = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    thres1, thres2, thres3, thres4, thres5, thres6, thres7, thres8, thres9, thres10, thres12, \
    thres14, thres16, thres18, thres20, thres20p = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    threshold, thres = [], []
    read_data()
    calc_core(30)
    threshold_add()
    print (threshold)
    print (thres)
    zhisun_calc()