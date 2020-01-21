import numpy as np
import copy
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self):
        self.learn_rate = 1
        self.t_data = None
        self.t_data_c = None
        self.w_b = np.array([[0],
                            [0],
                            [0]])

    def collect_data(self):
        collect_1 = []
        collect_2 = []
        while True:
            try:
                data = map(int, input("输入数据x1 x2 y（空格隔开)\
                输入任意字母敲回车以结束：").split(' '))
                data = list(data)
                collect_1.append(copy.copy(data))
                data[2] = 1
                collect_2.append(data)
            except ValueError:
                print("数据收集完毕！")
                break
        self.t_data = np.array(collect_1)
        self.t_data_c = np.array(collect_2)

    def gradient_descent(self):
        print("开始迭代...")
        while True:
            mistake = 0
            for line, line_c in zip(self.t_data, self.t_data_c):
                if line[2] * np.dot(line_c, self.w_b)[0] <= 0:
                    line_c = line_c * line[2]
                    mistake += 1
                    self.w_b[0][0] += line_c[0]
                    self.w_b[1][0] += line_c[1]
                    self.w_b[2][0] += line_c[2]
            if mistake == 0:
                break
        print("迭代完成！")

    def visualize(self):
        plt.figure(figsize=(8, 4))
        x = 0
        y = 0
        if not self.w_b[1][0]:
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


sss = Perceptron()
sss.collect_data()
sss.gradient_descent()
sss.visualize()
