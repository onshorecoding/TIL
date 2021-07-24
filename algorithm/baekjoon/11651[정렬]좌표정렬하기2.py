n = int(input())

lst = [tuple(map(int, input().split())) for _ in range(n)]

sorted_lst = sorted(lst, key=lambda x: (x[1], x[0]))

for x, y in sorted_lst:
    print(x, y)
