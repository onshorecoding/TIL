import sys
sys.setrecursionlimit(10000000)

N = int(input())
dic = {0:1, 1:-1, 2:-1, 3:1, 4:-1, 5:1}

def dp(n):
    if n in dic:
        return dic[n]
    else:
        if dp(n-3) != -1 and dp(n-5) != -1:
            dic[n] =  min(dp(n-3), dp(n-5))  + 1

        elif dp(n-3) == -1 and dp(n-5) != -1:
            dic[n] =  dp(n-5)  + 1

        elif  dp(n-3) != -1 and dp(n-5) == -1:
            dic[n] = dp(n-3) + 1
        else:
            dic[n] = -1
    return dic[n]

print(dp(N))

# N = int(input())
# dic = {0:1, 1:-1, 2:-1, 3:1, 4:-1, 5:1}

# def dp(n):
#     if n in dic:
#         return dic[n]
#     else:
#         dic[n] =  min(dp(n-3), dp(n-5))  + 1 
#     return dic[n]

# print(dp(N))