from itertools import permutations
from sys import stdin

N, M = map(int, input().split())

lst = list(map(int, stdin.readline().split()))

card = permutations(lst, 3)

check = 9999999

for i in card:
    b = sum(i)
    if M >= b:
        if (M - b) < check:
            check = M - b

print(M - check)
