n, k = map(int, input().split())
lst = list(map(int, input().split()))


s, e = 0, k
ans = temp = sum(lst[s:e])
while e < n:
    temp -= lst[s]
    s += 1
    e += 1
    temp += lst[e - 1]

    if temp > ans:
        ans = temp


print(ans)
