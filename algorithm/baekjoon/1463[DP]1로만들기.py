# import sys
# sys.setrecursionlimit(10000000)

# N = int(input())
# dic = {1:0, 2:1, 3:1}

# def dp (n):
#     if n in dic:
#         return dic[n]
#     else:
#         three = dp(n//3) if n%3 ==0 else 10000000
#         two = dp(n//2) if n%2 == 0 else 10000000
#         dic[n] =  min(three, two, dp(n-1)) +1

#     return dic[n]

# print(dp(N))

N = int(input())
dic = {1: 0, 2: 1}

for i in range(2, N + 1):
    dic[i] = dic[i - 1] + 1
    if i % 2 == 0:
        dic[i] = min(dic[i], dic[i // 2] + 1)
    if i % 3 == 0:
        dic[i] = min(dic[i], dic[i // 3] + 1)

print(dic[N])