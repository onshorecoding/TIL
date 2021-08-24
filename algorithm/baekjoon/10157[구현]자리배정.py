def check_seat(c, r):
    x, y = 1, 0
    cnt, idx = 0, 0
    r += 1

    while idx <= total:
        c -= 1
        r -= 1

        for _ in range(r):
            y += d[cnt % 2]
            idx += 1
            if idx == k:
                return x, y

        for _ in range(c):
            x += d[cnt % 2]
            idx += 1
            if idx == k:
                return x, y

        cnt += 1


c, r = map(int, input().split())
k = int(input())
d = [1, -1]
total = c * r

if k > total:
    print(0)
else:
    x, y = check_seat(c, r)
    print(x, y)
