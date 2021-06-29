from re import L


N = int(input())
lst = [int(input()) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1
    for j in range(i+1, N,-1):
        if int(max_i) < int(lst[j]):
            max_i = lst[j]
            dp[i][j] = max(dp[i][j-1]+1,)


print(dp)

