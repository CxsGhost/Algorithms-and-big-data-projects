disorder_list = input("input the list:").split(",")
list_1 = []


def turn_list():
    for j in disorder_list:
        list_1.append(float(j))
# 建立一个从小到大的排序方法


def Bubble_sort(array):
    i = 0
    while i <= length-2:
        if array[i] > array[i+1]:
            transfer = array[i]
            array[i] = array[i+1]
            array[i+1] = transfer
        i += 1
    return array


turn_list()
length = len(list_1)
number = 0
while number <= length-1:
    sorted_list = Bubble_sort(list_1)
    number += 1
else:
    print(sorted_list)
