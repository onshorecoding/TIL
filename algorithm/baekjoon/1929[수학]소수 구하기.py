m, n = map(int, input().split())

check = [True] * (n + 1)

e = int((n) ** 0.5)

for i in range(2, e + 1):
    if check[i] == True:
        for j in range(i * 2, n + 1, i):
            check[j] = False

ans = [str(i) for i in range(m, n + 1) if check[i] == True and i > 1]

print("\n".join(ans))