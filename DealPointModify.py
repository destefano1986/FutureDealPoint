# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

def read_data():
    global data
    data = pd.read_csv('data_day_coal.csv', encoding = 'gbk')
    data.columns = ['datetime', 'open', 'high', 'low', 'close', 'cjl', 'ccl']


#定义点位支撑位
def zhichengwei_point(int1, percentage, num):
    global data
    lst = []
    #不同K线情况下参数需进行微调
    for i in range(60, (len(data)-60)):
        count = -1
        tag = 0
        for j in range(-int1, 0):
            if data.loc[i + j, 'low'] >= data.loc[i, 'low']*(1 - percentage/100) and \
                    data.loc[i + j, 'low'] <= data.loc[i, 'low']*(1 + percentage/100):
                count = count + 1
            if data.loc[i + j, 'low'] <= data.loc[i, 'low']*(1 - percentage/100):
                tag = tag + 1
        record = dict(index = i, point = data.loc[i,'low'], count = count)
        if count >= num and tag == 0:
            lst.append(record)
    return lst


#定义点位阻力位
def zuliwei_point(int1, percentage, num):
    global data
    lst = []
    for i in range(60, (len(data)-60)):
        count = -1
        tag = 0
        for j in range(-int1, 0):
            if data.loc[i + j, 'high'] <= data.loc[i, 'high']*(1 + percentage/100) and \
                    data.loc[i + j, 'high'] >= data.loc[i, 'high']*(1 - percentage/100):
                count = count + 1
            if data.loc[i + j, 'high'] >= data.loc[i, 'high']*(1 + percentage/100):
                tag = tag + 1
        record = dict(index = i, point = data.loc[i,'high'], count = count)
        if count >= num and tag == 0:
            lst.append(record)
    return lst


#定义均线支撑位
def zhichengwei_line(int1, percentage, num):
    global data
    lst = []
    for i in range(60, (len(data)-60)):
        price = data.loc[i-int1:i, 'close']
        avg = np.mean(price)
        count = 0
        tag = 0
        for j in range(-int1, 0):
            if data.loc[i + j, 'low'] >= np.mean(data.loc[i + j - int1:i + j, 'close'])*(1 - percentage/100) and \
                    data.loc[i + j, 'low'] <= np.mean(data.loc[i + j - int1:i + j, 'close'])*(1 + percentage/100):
                count = count + 1
            if data.loc[i + j, 'low'] <= np.mean(data.loc[i + j - int1:i + j, 'close'])*(1 - percentage/100):
                tag = tag + 1
        record = dict(index = i, point = avg, count = count)
        if count >= num and tag == 0:
            lst.append(record)
    return lst


#定义均线阻力位
def zuliwei_line(int1, percentage, num):
    global data
    lst = []
    for i in range(60, (len(data)-60)):
        price = data.loc[i-int1:i, 'close']
        avg = np.mean(price)
        count = 0
        tag = 0
        for j in range(-int1, 0):
            if data.loc[i + j, 'high'] <= np.mean(data.loc[i + j - int1:i + j, 'close'])*(1 + percentage/100) and \
                    data.loc[i + j, 'high'] >= np.mean(data.loc[i + j - int1:i + j, 'close'])*(1 - percentage/100):
                count = count + 1
            if data.loc[i + j, 'high'] >= np.mean(data.loc[i + j - int1:i + j, 'close'])*(1 + percentage/100):
                tag = tag + 1
        record = dict(index = i, point = avg, count = count)
        if count >= num and tag == 0:
            lst.append(record)
    return lst


#上述参数需优化
def calc_core(int2, int3, type, direction, percentage):
    global para, data
    global threshold05, threshold10, threshold15, threshold20, threshold25, threshold30, threshold35, threshold40, threshold45, threshold50, threshold50p
    global thres1, thres2, thres3, thres4, thres5, thres6, thres7, thres8, thres9, thres10, thres10p, thres15p, thres20p
    global threshold, thres
    for i in range(0, len(para)):
        tmp = 0
        buffer = 0
        tmpcc = 0
        if (type == 'zcw') & (direction == 'bear'):
            for j in range(0, int2):
                if data.loc[para.loc[i, 'index'] + j + 1, 'low'] < para.loc[i, 'point'] * (1 - percentage / 100):
                    buffer = buffer + 1
            if buffer > 0:
                for j in range(0, int2):
                    maximum = (data.loc[para.loc[i, 'index'] + j + 1, 'high'] - para.loc[i, 'point'] * (1 - percentage / 100)) / (para.loc[i, 'point'] * (1 - percentage / 100))
                    if maximum > tmp:
                        tmp = maximum
            if tmp <= 0.005 and tmp > 0:
                threshold05 = threshold05 + 1
            elif tmp <= 0.01 and tmp > 0.005:
                threshold10 = threshold10 + 1
            elif tmp <= 0.015 and tmp > 0.01:
                threshold15 = threshold15 + 1
            elif tmp <= 0.02 and tmp > 0.015:
                threshold20 = threshold20 + 1
            elif tmp <= 0.025 and tmp > 0.02:
                threshold25 = threshold25 + 1
            elif tmp <= 0.03 and tmp > 0.025:
                threshold30 = threshold30 + 1
            elif tmp <= 0.035 and tmp > 0.03:
                threshold35 = threshold35 + 1
            elif tmp <= 0.04 and tmp > 0.035:
                threshold40 = threshold40 + 1
            elif tmp <= 0.045 and tmp > 0.04:
                threshold45 = threshold45 + 1
            elif tmp <= 0.05 and tmp > 0.045:
                threshold50 = threshold50 + 1
            elif tmp > 0.05:
                threshold50p = threshold50p + 1
            if buffer > 0:
                for k in range(0, int3):
                    money = (para.loc[i, 'point'] * (1 - percentage / 100) - data.loc[para.loc[i, 'index'] + k + 1, 'low']) / data.loc[para.loc[i, 'index'] + k + 1, 'low']
                    if money > tmpcc:
                        tmpcc = money
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
            elif tmpcc <= 0.15 and tmpcc > 0.1:
                thres10p = thres10p + 1
            elif tmpcc <= 0.2 and tmpcc > 0.15:
                thres15p = thres15p + 1
            elif tmpcc > 0.2:
                thres20p = thres20p + 1
        if (type == 'zcw') & (direction == 'bull'):
            for j in range(0, int2):
                if data.loc[para.loc[i, 'index'] + j + 1, 'high'] > para.loc[i, 'point'] * (1 + percentage / 100):
                    buffer = buffer + 1
            if buffer > 0:
                for j in range(0, int2):
                    maximum = (para.loc[i, 'point'] * (1 + percentage / 100) - data.loc[para.loc[i, 'index'] + j + 1, 'low']) / data.loc[para.loc[i, 'index'] + j + 1, 'low']
                    if maximum > tmp:
                        tmp = maximum
            if tmp <= 0.005 and tmp > 0:
                threshold05 = threshold05 + 1
            elif tmp <= 0.01 and tmp > 0.005:
                threshold10 = threshold10 + 1
            elif tmp <= 0.015 and tmp > 0.01:
                threshold15 = threshold15 + 1
            elif tmp <= 0.02 and tmp > 0.015:
                threshold20 = threshold20 + 1
            elif tmp <= 0.025 and tmp > 0.02:
                threshold25 = threshold25 + 1
            elif tmp <= 0.03 and tmp > 0.025:
                threshold30 = threshold30 + 1
            elif tmp <= 0.035 and tmp > 0.03:
                threshold35 = threshold35 + 1
            elif tmp <= 0.04 and tmp > 0.035:
                threshold40 = threshold40 + 1
            elif tmp <= 0.045 and tmp > 0.04:
                threshold45 = threshold45 + 1
            elif tmp <= 0.05 and tmp > 0.045:
                threshold50 = threshold50 + 1
            elif tmp > 0.05:
                threshold50p = threshold50p + 1
            if buffer > 0:
                for k in range(0, int3):
                    money = (data.loc[para.loc[i, 'index'] + k + 1, 'high'] - para.loc[i, 'point'] * (1 + percentage / 100)) / (para.loc[i, 'point'] * (1 + percentage / 100))
                    if money > tmpcc:
                        tmpcc = money
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
            elif tmpcc <= 0.15 and tmpcc > 0.1:
                thres10p = thres10p + 1
            elif tmpcc <= 0.2 and tmpcc > 0.15:
                thres15p = thres15p + 1
            elif tmpcc > 0.2:
                thres20p = thres20p + 1
        if (type == 'zlw') & (direction == 'bull'):
            for j in range(0, int2):
                if data.loc[para.loc[i, 'index'] + j + 1, 'high'] > para.loc[i, 'point'] * (1 + percentage / 100):
                    buffer = buffer + 1
            if buffer > 0:
                for j in range(0, int2):
                    maximum = (para.loc[i, 'point'] * (1 + percentage / 100) - data.loc[para.loc[i, 'index'] + j + 1, 'low']) / data.loc[para.loc[i, 'index'] + j + 1, 'low']
                    if maximum > tmp:
                        tmp = maximum
            if tmp <= 0.005 and tmp > 0:
                threshold05 = threshold05 + 1
            elif tmp <= 0.01 and tmp > 0.005:
                threshold10 = threshold10 + 1
            elif tmp <= 0.015 and tmp > 0.01:
                threshold15 = threshold15 + 1
            elif tmp <= 0.02 and tmp > 0.015:
                threshold20 = threshold20 + 1
            elif tmp <= 0.025 and tmp > 0.02:
                threshold25 = threshold25 + 1
            elif tmp <= 0.03 and tmp > 0.025:
                threshold30 = threshold30 + 1
            elif tmp <= 0.035 and tmp > 0.03:
                threshold35 = threshold35 + 1
            elif tmp <= 0.04 and tmp > 0.035:
                threshold40 = threshold40 + 1
            elif tmp <= 0.045 and tmp > 0.04:
                threshold45 = threshold45 + 1
            elif tmp <= 0.05 and tmp > 0.045:
                threshold50 = threshold50 + 1
            elif tmp > 0.05:
                threshold50p = threshold50p + 1
            if buffer > 0:
                for k in range(0, int3):
                    money = (data.loc[para.loc[i, 'index'] + k + 1, 'high'] - para.loc[i, 'point'] * (1 + percentage / 100)) / (para.loc[i, 'point'] * (1 + percentage / 100))
                    if money > tmpcc:
                        tmpcc = money
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
            elif tmpcc <= 0.15 and tmpcc > 0.1:
                thres10p = thres10p + 1
            elif tmpcc <= 0.2 and tmpcc > 0.15:
                thres15p = thres15p + 1
            elif tmpcc > 0.2:
                thres20p = thres20p + 1
        if (type == 'zlw') & (direction == 'bear'):
            for j in range(0, int2):
                if data.loc[para.loc[i, 'index'] + j + 1, 'low'] < para.loc[i, 'point'] * (1 - percentage / 100):
                    buffer = buffer + 1
            if buffer > 0:
                for j in range(0, int2):
                    maximum = (data.loc[para.loc[i, 'index'] + j + 1, 'high'] - para.loc[i, 'point'] * (1 - percentage / 100)) / (para.loc[i, 'point'] * (1 - percentage / 100))
                    if maximum > tmp:
                        tmp = maximum
            if tmp <= 0.005 and tmp > 0:
                threshold05 = threshold05 + 1
            elif tmp <= 0.01 and tmp > 0.005:
                threshold10 = threshold10 + 1
            elif tmp <= 0.015 and tmp > 0.01:
                threshold15 = threshold15 + 1
            elif tmp <= 0.02 and tmp > 0.015:
                threshold20 = threshold20 + 1
            elif tmp <= 0.025 and tmp > 0.02:
                threshold25 = threshold25 + 1
            elif tmp <= 0.03 and tmp > 0.025:
                threshold30 = threshold30 + 1
            elif tmp <= 0.035 and tmp > 0.03:
                threshold35 = threshold35 + 1
            elif tmp <= 0.04 and tmp > 0.035:
                threshold40 = threshold40 + 1
            elif tmp <= 0.045 and tmp > 0.04:
                threshold45 = threshold45 + 1
            elif tmp <= 0.05 and tmp > 0.045:
                threshold50 = threshold50 + 1
            elif tmp > 0.05:
                threshold50p = threshold50p + 1
            if buffer > 0:
                for k in range(0, int3):
                    money = (para.loc[i, 'point'] * (1 - percentage / 100) - data.loc[para.loc[i, 'index'] + k + 1, 'low']) / data.loc[para.loc[i, 'index'] + k + 1, 'low']
                    if money > tmpcc:
                        tmpcc = money
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
            elif tmpcc <= 0.15 and tmpcc > 0.1:
                thres10p = thres10p + 1
            elif tmpcc <= 0.2 and tmpcc > 0.15:
                thres15p = thres15p + 1
            elif tmpcc > 0.2:
                thres20p = thres20p + 1


def threshold_add():
    global threshold05, threshold10, threshold15, threshold20, threshold25, threshold30, threshold35, threshold40, threshold45, threshold50, threshold50p
    global thres1, thres2, thres3, thres4, thres5, thres6, thres7, thres8, thres9, thres10, thres10p, thres15p, thres20p
    global threshold, thres
    threshold.append(threshold05)
    threshold.append(threshold10)
    threshold.append(threshold15)
    threshold.append(threshold20)
    threshold.append(threshold25)
    threshold.append(threshold30)
    threshold.append(threshold35)
    threshold.append(threshold40)
    threshold.append(threshold45)
    threshold.append(threshold50)
    threshold.append(threshold50p)
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
    thres.append(thres10p)
    thres.append(thres15p)
    thres.append(thres20p)


def zhisun_calc():
    global threshold
    zssum = 0
    for zhisun in range(0, 11):
        zssum = zssum + threshold[zhisun]
        zsprob = zssum / sum(threshold)
        print ('zhisun probability: ' + str(zhisun/2 + 0.5 ) + '    ' + str(zsprob))


def zhiying_calc():
    global thres
    zysum = 0
    for zhiyin in range(0, 13):
        zysum = zysum + thres[zhiyin]
        zyprob = zysum / sum(thres)
        print ('zhiyin probability: ' + str(zhiyin) + '    ' + str(zyprob))
    zyall = (0.5*thres[0]+1.5*thres[1]+2.5*thres[2]+3.5*thres[3]+4.5*thres[4]+5.5*thres[5]+6.5*thres[6]+7.5*thres[7]+ \
            8.5*thres[8]+9.5*thres[9]+12.5*thres[10]+17.5*thres[11]+22.5*thres[12])*0.7/sum(thres)
    print ('zhiyin expectation: ' + str(zyall))


if __name__ == "__main__":
    read_data()
    # 如下函数参数需优化
    para = zhichengwei_point(20, 3, 0.5)
    para = pd.DataFrame(para)
    # 如下重要参数需优化
    int2 = 30
    int3 = 30
    type = 'zcw'
    direction = 'bear'

    percentage = 1.0
    # 止损止盈点确认
    # 求解在遍历percentage下的准确率
    threshold05, threshold10, threshold15, threshold20, threshold25, threshold30, threshold35, threshold40, threshold45, threshold50, threshold50p = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    threshold = []
    thres1, thres2, thres3, thres4, thres5, thres6, thres7, thres8, thres9, thres10, thres10p, thres15p, thres20p = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    thres = []
    calc_core(int2, int3, type, direction, percentage)
    threshold_add()
    print(threshold)
    print(thres)
    zhisun_calc()
    zhiying_calc()
    '''
    #循环优化percentage
    for percentage in [0.5, 1.0, 1.5 ,2.0, 2.5, 3.0]:
        threshold05, threshold10, threshold15, threshold20, threshold25, threshold30, threshold35, threshold40, threshold45, threshold50, threshold50p = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        threshold = []
        thres1, thres2, thres3, thres4, thres5, thres6, thres7, thres8, thres9, thres10, thres10p, thres15p, thres20p = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        thres = []
        calc_core(int2, int3, type, direction, percentage)
        threshold_add()
        print ('**********dealing: ' + str(percentage) + ' now...**********')
        print(threshold)
        print(thres)
        zhisun_calc()
        
    '''