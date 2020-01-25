import pandas as pd
import numpy as np
import re
import copy


data = np.array(pd.read_csv('housing.csv', header=None))
data_1 = []
for i in range(len(data)):
    data_2 = re.findall(r'\d+\.?\d*', data[i][0])  # 提取所有的数字
    data_1.append(list(map(float, data_2)))  # 把数据转化为浮点数
data_1 = np.array(data_1, dtype='float64')  # 转换为矩阵
y = np.array([[_y] for _y in copy.copy(data_1[:, 13])], dtype='float64')  # 把房价y取出来用于后续迭代计算
data_1 = np.delete(data_1, -1, axis=1)  # 删除最后一列


def normalize(_d):  # 归一化
    return (_d - _min) / (_max - _min)


for line in range(len(data_1[0])):  # 归一化
    _max = max(data_1[:, line])
    _min = min(data_1[:, line])
    data_1[:, line] = list(map(normalize, data_1[:, line]))

_b = [1 for j in range(len(data_1))]
data_1 = np.insert(data_1, len(data_1[0]), values=_b, axis=1)  # 在最后添加一列1，来乘b

w = np.array([[0] for k in range(len(data_1[0]))], dtype='float64')  # 创建初始参数矩阵
l_rate = 0.01


# 求偏导数并开始梯度下降迭代
number = 0
while number < 100000:
    w_c = copy.copy(w)  # 因为参数要同时更新，新建一个副本来实现
    for d in range(13):
        w_c[d][0] -= l_rate * np.dot(data_1[:, d], np.dot(data_1, w) - y)[0] / len(data_1)  # 根据偏导数，写成矩阵实现，感觉既然没报错，应该就是对的啊。。e而且也检查过公式了
    w_c[13][0] -= l_rate * np.dot(np.array(_b), np.dot(data_1, w) - y)[0] / len(data_1)
    w = w_c
    number += 1
    print(w)
