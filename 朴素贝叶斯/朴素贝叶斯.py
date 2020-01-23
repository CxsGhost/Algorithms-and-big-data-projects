import numpy as np
from collections import Counter


class Bayes:
    def __init__(self):
        self.t_data = np.array([[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
                                ['S', 'M', 'M', 'S', 'S', 'S', 'M', 'M', 'L', 'L', 'L', 'M', 'M', 'L', 'L'],
                                [-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1]])
        self.p_y = {}
        self.p_x1_y = {}  # 使用字典方便计算时调用
        self.p_x2_y = {}

    def learning(self):
        count_y = Counter(self.t_data[2])  # 统计y的种类及数量，用于后续计算
        ys = {}  # 使该二维分类器不局限于两种类（y）（不失一般性），接下来先统计y的种类，并计算概率，再切分训练数据
        for y in count_y.keys():
            ys[y] = []
            self.p_y[y] = count_y[y] / len(self.t_data[0])  # 计算先验概率并对应y值存入字典
        for i in range(len(self.t_data[0])):
            ys[self.t_data[2][i]].append(self.t_data[:, i])  # 将数据切分后分别存入字典，key是对应的y值
        print('数据处理完成，开始学习...')
        for item in ys.items():
            self.calculate(item)
        print('学习完毕！可以开始预测')

    def calculate(self, _y):
        data = np.array(_y[1])  # 先把数据转化为矩阵，便于接下来切片统计运算
        count_x1 = Counter(data[:, 0])
        count_x2 = Counter(data[:, 1])
        for x1 in count_x1.keys():  # 计算相应的概率，存入字典
            self.p_x1_y['{}_{}'.format(x1, _y[0])] = count_x1[x1] / len(data)
        for x2 in count_x2.keys():
            self.p_x2_y['{}_{}'.format(x2, _y[0])] = count_x2[x2] / len(data)

    def analyse_input(self):  # 计算后验概率并比较
        in_data = input('输入x1, x2（空格隔开）：').split(' ')
        p_p = 0
        result = []
        for j in self.p_y.keys():
            pp = self.p_y[j] * self.p_x1_y['{}_{}'.format(in_data[0], j)] *\
                 self.p_x2_y['{}_{}'.format(in_data[1], j)]
        #     if pp >= p_p:  # 观察到，对于相同的输入，可能出现两种不同预测结果（对于本次数据来说，只有两种结果），要对此做处理
        #         if p_p < pp:  # 若有出现更大的概率，需要把先前已有的所有结果全部替换
        #             if not result:  # 开始的时候列表是空的，如果直写循环替换，其实那个循环根本不会开始。如果在循环后添加，那将会导致接下来有的结果会重复进入列表（被替换的和被添加的）
        #                 result.append(j)  # 所以必须额外加这一个判断（其实我觉得我这里搞麻烦了。。但是也没想到什么好的解决办法）
        #             else:
        #                 for r in range(len(result)):
        #                     result[r] = j
        #         if p_p == pp:
        #             result.append(j)
        #         p_p = pp
        # if len(result) == 1:
        #     print('预测结果为：{}'.format(result[0]))
        # else:
        #     print('可能结果为以下几种：', end='')
        #     for e in result:
        #         print(e)

        # 以上是我的判断失误。。但是我觉得在别的数据中可能会出现吧

            if pp > p_p:
                p_p = pp
                result.append(j)
        print('预测结果为：{}'.format(result[0]))


b = Bayes()
b.learning()
b.analyse_input()


