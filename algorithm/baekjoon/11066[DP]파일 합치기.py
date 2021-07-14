def dp(n, lst, a):

    if n == 1:
        a[1] = lst[0] + lst[1]
        return a[1]
    else:
        a[n] = dp(n - 1, lst, a) + lst[n]
        return a[n]


N = int(input())
book, data, ans = [], [], []

for i in range(N):
    book.append(int(input()))
    data.append(sorted(list(map(int, input().split()))))

for bookdata in data:
    a = [0] * len(bookdata)
    dp(len(bookdata) - 1, bookdata, a)
    print(a)
    ans.append(sum(a))

print(ans)
