from collections import Counter

N = int(input())
lst = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

lst = Counter(lst)

for n in check:
    print(lst[n], end=" ")