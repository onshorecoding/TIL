k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]

s, e = 1, max(lst)
ans = 0

while s <= e:
    m = (s + e) // 2
    cnt = 0
    for l in lst:
        cnt += l // m

    if n <= cnt:
        ans = max(ans, m)
        s = m + 1
    else:
        e = m - 1

print(ans)
