import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
for line in a:
    print(line)
b = np.array([[1],
              [1],
              [1]])
print(-1*np.dot(a[1], b)[0] <= 0)

d = [1, 2, 3]
k = ["w", "e", "y"]
for i in zip(d, k):
    print(i)
    #print(j)
