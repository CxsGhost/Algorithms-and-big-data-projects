
import time
a= time.time()


T = int(input())
list_dc = [[] for _ in range(T)]
for t in range(T):
    n = int(input())
    list_dc[t] = list(map(int, input().strip().split(' ')))


def Recursion(du):
    length = len(du) - 1
    for m in range(1000):
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
        return 'ZERO'


result = map(Recursion, list_dc)
for i in result:
    print(i)

print(time.time() - a)

