x, y, m, h = map(int, input().split())
print(min(x,y, m-x, h-y))