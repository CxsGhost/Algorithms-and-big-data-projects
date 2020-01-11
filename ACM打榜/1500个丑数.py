list_ugly = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]


def q_find(list_3, theta_1):
    mid = int(len(list_3) / 2)
    if list_3[mid] <= theta_1:
        if list_3[mid] == theta_1 or list_3[mid + 1] > theta_1:
            return list_3[mid + 1]
        else:
            list_4 = list_3[mid + 1:]
            return q_find(list_4, theta_1)
    if list_3[mid] > theta_1:
        if list_3[mid - 1] <= theta_1:
            return list_3[mid]
        else:
            list_5 = list_3[:mid]
            return q_find(list_5, theta_1)


def multiplication(n):
    theta = list_ugly[len(list_ugly) - 1]
    x = lambda i: i * n
    list_k = list(map(x, list_ugly))
    return q_find(list_k, theta)


def find_next():
    number = list(map(multiplication, [2, 3, 5]))
    return min(number)


def Ugly_1500():
    while len(list_ugly) < 1500:
        _next = find_next()
        list_ugly.append(_next)
    return "The 1500'th ugly number is {}.".format(list_ugly.pop())


print(Ugly_1500())







