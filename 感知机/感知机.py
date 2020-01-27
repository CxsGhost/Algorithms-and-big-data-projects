import numpy as np
import copy
import matplotlib.pyplot as plt

# 创建numpy数组必须声明浮点数类型，否则当学习率不为1时，会导致参数更新自动取整，进而会出现迭代无法完成的情况
# 包括收录数据时，也要声明为浮点类型，否则就导致数据自动变为取整型int32


class Perceptron:
    def __init__(self):
        self.learn_rate = 0.5  # 随意设置
        self.w_b = np.array([[0],
                            [0],
                            [0]], dtype='float32')  # 把三个参数放在一个矩阵中（w1, w2, b）
        self.t_data = None
        self.t_data_c = None  # 因为要三个参数一起更新，观察书上的公式，其实就是y乘x1,x2,1,然后加到参数矩阵就行了所以又建立一个y值全是1的矩阵

    def collect_data(self):
        collect_1 = []
        collect_2 = []
        while True:
            try:  # 利用异常处理结束输入，别的没想到啥好办法。。
                data = map(float, input("输入数据x1 x2 y（空格隔开)\
                输入任意字母敲回车以结束：").split(' '))
                data = list(data)
                collect_1.append(copy.copy(data))  # 测试发现，下一行的更改会影响上一行，两个指向的变量地址一样，所以得copy一下
                data[2] = 1
                collect_2.append(data)
            except ValueError:
                print("数据收集完毕！")
                break
        self.t_data = np.array(collect_1, dtype='float32')
        self.t_data_c = np.array(collect_2, dtype='float32')

    def gradient_descent(self):
        print("开始迭代...")
        number = 0
        while True:
            number += 1
            # 每次都统计误分类的点数，直到没有为止，跳出循环，迭代结束
            mistake = 0
            for line, line_c in zip(self.t_data, self.t_data_c):  # 一个用来判断是否误分类，一个用来更新参数矩阵
                if line[2] * np.dot(line_c, self.w_b)[0] <= 0:
                    line_c = line_c * line[2] * self.learn_rate  # 更新方法对应着上面第二条注释
                    print(line_c)
                    mistake += 1
                    self.w_b[0][0] += line_c[0]
                    self.w_b[1][0] += line_c[1]
                    self.w_b[2][0] += line_c[2]
            if mistake == 0:
                break
            print('第{}次迭代\n参数w：{}'.format(number, self.w_b))
        print('-----------------')
        print("迭代完成！")
        print('本次学习率：{}，迭代次数：{}'.format(self.learn_rate, number))

    def visualize(self):  # 以下绘图中的y并不是之前的那个y,其实是所谓的x_2。。
        plt.figure(figsize=(8, 4))
        x = 0
        y = 0
        if not self.w_b[1][0]:  # 测试中发现，出现了x_2的系数为0的情况，这样的话绘图时就相当于除数为0了
            x = -1 * self.w_b[2][0] / self.w_b[0][0]
            plt.axvline(x, color='g')
        else:
            x = np.linspace(-10, 10, 10)
            y = -1 * self.w_b[0][0] / self.w_b[1][0] * x + -1 * self.w_b[2][0] / self.w_b[1][0]
            plt.plot(x, y, color='g')
        for i in self.t_data:
            if i[2] == 1:
                plt.scatter(i[0], i[1], c='r', s=5)
            else:
                plt.scatter(i[0], i[1], c='b', s=5)
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.xlabel('x(1)')
        plt.ylabel('x(2)')
        plt.show()


p = Perceptron()
p.collect_data()
p.gradient_descent()
p.visualize()
