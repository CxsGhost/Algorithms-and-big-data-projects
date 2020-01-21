from re import split
from sys import stdin


def Dict():
    str_1 = stdin.read()
    str_2 = str_1.lower()
    str_3 = set(split(r'[^a-z]', str_2))
    for i in sorted(str_3):
        if i:
            print(i)


Dict()




import string


def wash_data(s):
    for k in string.punctuation:
        s = s.replace(k, " ")
    for n in range(10):
        s = s.replace(str(n), " ")
    list_1 = s.lower().split(' ')
    set_1 = set(list_1)
    return set_1


list_str = []  # 用于收集字符串
set_all = set()  # 先建立里一个空集合，后续合并时使用
while True:
    try:
        str_ = input()
        list_str.append(str_)
    except EOFError:
        break
list_set = map(wash_data, list_str)
for i in list_set:
    set_all = set_all | i
for j in sorted(set_all):
    print(j)
