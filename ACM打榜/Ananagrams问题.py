from collections import Counter


list_raw = []
while True:
    _str = input()
    if _str == "#":
        break
    else:
        list_raw.extend(list(_str.split(' ')))


def Lower(s_1):
    return s_1.lower()


def Sort(s_2):
    return ''.join(sorted(s_2))


def Find(s_3):
    if s_3[1] == 1:  # 检查字幕组是不是唯一的，唯一的则根据排序后字母组索引，返回最初列表中的单词
        return list_raw[list_sort.index(s_3[0])]


list_low = map(Lower, list_raw)
list_sort = list(map(Sort, list_low))
number = Counter(list_sort).items()
ana = list(filter(None, map(Find, number)))  # 过滤器过滤掉其中的None，因为单词组不唯一的单词组函数无返回值
for i in sorted(ana):
    print(i)


