from sys import stdin

# input = stdin.readline()

n = int(input())
lst = list(map(int, input().split()))
sorted_lst = sorted(set(lst))

lst_dct = {}
for i in range(len(sorted_lst)):
    lst_dct[sorted_lst[i]] = i

for num in lst:
    print(lst_dct[num], end=" ")