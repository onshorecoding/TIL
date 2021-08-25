w, j = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x_d, x_m = divmod(p + t, w)
y_d, y_m = divmod(q + t, j)

if x_d % 2:
    x = w - x_m
else:
    x = x_m
if y_d % 2:
    y = j - y_d
else:
    y = y_d


print(x, y)
