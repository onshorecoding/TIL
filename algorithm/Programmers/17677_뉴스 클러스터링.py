from collections import Counter


def make_list(string):
    str_lst = []

    for i in range(1, len(string)):
        str_set = string[i - 1 : i + 1]
        if str_set.isalpha():
            str_lst.append(str_set)
    print(string, str_lst)
    return str_lst


def calculate_jaccard(lst1, lst2):
    set1 = Counter(lst1)
    set2 = Counter(lst2)

    mom = 0
    child = 0

    for key, value in set1.items():
        if key in set2:
            mom += max(value, set2[key])
            child += min(value, set2[key])
        else:
            mom += value

    for key, value in set2.items():
        if key not in set1:
            mom += value

    return child / mom


def solution(str1, str2):
    answer = 65536
    str1 = str1.lower()
    str2 = str2.lower()

    str1_lst = make_list(str1)
    str2_lst = make_list(str2)

    if not str1_lst and not str2_lst:
        return answer
    else:
        return int(calculate_jaccard(str1_lst, str2_lst) * answer)
