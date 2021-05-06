def dfs(m,n, map):
    checked = []
    for i in range(m-1):
        for j in range(n-1, -1):
            if k_map[i][j] != 0:
                if k_map[i][j] == k_map[i][j+1] and  k_map[i][j] == k_map[i+1][j] and k_map[i][j] == k_map[i+1][j+1]:
                    checked.append([i,j])

    
    return k_map

def solution(m, n, board):
    answer = 0
    k_map = [[0]*m for i in range(n)]
    
    for i in range(m):
        for j in range(n):
            k_map[i][j]= board[i][j]
    
    while True:

        new_map = dfs(m,n, k_map)
        
        if new_map == k_map:
            break
        else:
            k_map = new_map



    return answer