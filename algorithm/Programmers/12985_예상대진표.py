from math import log


def solution(n, a, b):
    ind = int(log(n, 2))
    mid = n // 2

    if a <= mid and b <= mid:
        return solution(mid, a, b)
    elif a > mid and b > mid:
        return solution(mid, a - mid, b - mid)
    else:
        return ind


print(solution(8, 1, 2))