n = int(input())

ans = 0
dot_lst = [tuple(map(int, input().split())) for _ in range(n)]
l = len(dot_lst)

height = sorted(dot_lst, key = lambda x: (x[0], x[1]))

for i in range(0,l-1,2):
    ans += height[i+1][1] - height[i][1]

width = sorted(dot_lst, key = lambda x: (x[1], x[0]))

for i in range(0,l-1,2):
    ans += width[i+1][0] - width[i][0]

print(ans)

