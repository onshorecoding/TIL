N, M = map(int, input().split())

def solution():
    if N % M == 0 :
        return 0

    elif M % N == 0:
        return min((M//N-1) * N, M-1)
    
    else:
        return M-1


print(solution())