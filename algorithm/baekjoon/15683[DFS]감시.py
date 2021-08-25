def cctv(x, y, list: lst):
    if 1 in lst:  # 우측
        while y < m - 1:
            y += 1
            if lst[x][y] != 0:
                break
            else:
                lst[x][y] = "#"

    elif 2 in lst:  # 좌측
        while 0 < y:
            y -= 1
            if lst[x][y] != 0:
                break
            else:
                lst[x][y] = "#"
    elif 3 in lst:  # 상
        while x < n - 1:
            x += 1
            if lst[x][y] != 0:
                break
            else:
                lst[x][y] = "#"
    elif 4 in lst:
        while 0 < x:
            x -= 1
            if lst[x][y] != 0:
                break
            else:
                lst[x][y] = "#"


def count_square(lst):
    while lst:
        x, y, cctv_type = lst.pop()


n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
cctv_lst = [1, 2, 3, 4, 5]
stack = []

total = n * m
square = 0
wall = 0
max_cnt = 0

for i in range(n):
    for j in range(m):
        if lst[i][j] in cctv_lst:
            stack.append((n, m, lst[i][j]))
        if lst[i][j] == "0":
            square += 1
        if lst[i][j] == "6":
            wall += 1

stack.sort(key=lambda x: x[2])
