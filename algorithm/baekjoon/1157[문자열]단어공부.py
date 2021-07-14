from collections import Counter


def solution():

    w = input().upper()
    lst = Counter(w).most_common()

    if len(lst) == 1:
        return lst[0][0]

    if lst[0][1] == lst[1][1]:
        return "?"
    else:
        return lst[0][0]


print(solution())