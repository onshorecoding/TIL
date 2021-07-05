#누적합으로 품
N, H = map(int, input().split())

up = [0] * (H + 1)
down = [0] * (H + 1)
total = [0] * (H + 1)

for i in range(N):
    h = int(input())
    if i % 2:
        up[h] += 1
    else:
        down[H-h+1] += 1

for i in range(H-1, 0 , -1):
    up[i] += up[i+1]

for i in range(1, H+1):
    down[i] += down[i-1]

for i in range(1,H+1):
    total[i] = up[i] + down[i]

total = total[1:]
ans = min(total)
cnt = total.count(ans)

print(ans, cnt)

