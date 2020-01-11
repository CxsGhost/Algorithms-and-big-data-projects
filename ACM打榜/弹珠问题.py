from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)


def quick_sort(L):
    return q_sort(L, 0, len(L) - 1)


def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L


def Partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left


def find_position(_q, right, left=0):
    mid = int((right + left) / 2)
    if left > right:
        return "{} not found".format(_q)
    elif list_N[mid] == _q:
        posi = mid
        while list_N[posi - 1] == _q:
            posi -= 1
        return "{} found at {}".format(_q, posi + 1)
    elif list_N[mid] > _q:
        return find_position(_q, mid - 1, left)
    else:
        return find_position(_q, right, mid + 1)


list_N = []
list_Q = []
_right = []
number = 1
while True:
    N, Q = map(int, stdin.readline().split(' '))
    if N == 0 and Q == 0:
        break
    length = N - 1
    print("CASE# {}:".format(number))
    number += 1
    for l in range(N):
        list_N.append(int(stdin.readline()))
    list_N = quick_sort(list_N)
    for h in range(Q):
        _right.append(length)
        list_Q.append(int(stdin.readline()))
    result = map(find_position, list_Q, _right)
    for re in result:
        print(re)


