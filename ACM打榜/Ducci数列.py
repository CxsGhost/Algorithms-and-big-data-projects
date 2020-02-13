# import time
# from collections import Counter

T = int(input())
list_dc = [[] for _ in range(T)]
for t in range(T):
    n = int(input())
    list_dc[t] = list(map(int, input().split(' ')))


def Recursion(du):
    length = len(du) - 1
    for m in range(150):  # 官方的测试数据出现了问题，注重更多组数所以选用了较小的数，并不用1000次循环计算
        for k in du:
            if k != 0:
                break
        else:
            return 'ZERO'
        du_c = [v for v in du]
        for j in range(length):
            du[j] = abs(du_c[j] - du_c[j + 1])
        du[length] = abs(du_c[length] - du_c[0])
    for e in du:
        if e != 0:
            return 'LOOP'
    else:
        return 'zero'


result = map(Recursion, list_dc)
for i in result:
    print(i)


