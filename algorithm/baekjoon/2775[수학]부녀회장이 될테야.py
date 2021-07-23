t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    lst = [[i for i in range(1, n + 1)]]
    for i in range(1, k + 1):
        flr = []
        for j in range(n):
            flr.append(sum(lst[-1][: j + 1]))
        lst.append(flr)
    print(lst[-1][-1])