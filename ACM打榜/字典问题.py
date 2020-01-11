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


def combine(s):
    for k in string.punctuation:
        s = s.replace(k, " ")
    for n in range(10):
        s = s.replace(str(n), " ")
    list_1 = s.lower().split(' ')
    set_1 = set(list_1)
    return set_1


list_str = []
set_all = set()
while True:
    try:
        str_ = input()
        list_str.append(str_)
    except EOFError:
        break
list_set = map(combine, list_str)
for i in list_set:
    set_all = set_all | i
list_dic = list(set_all)
list_dic.sort()
for j in list_dic:
    print(j)
