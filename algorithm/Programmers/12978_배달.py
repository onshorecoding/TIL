
# 시간초과 미해결

from collections import deque

def solution(N, road, K):
    answer = 0
    road_map = [[500000] * (N+1) for i in range(N+1)]
    visited = [False] * (N+1)
    dq =deque([])
    
    for i in road:
        if i[2] <= K:
            if i[0] == 1:
                dq.append([i[1],i[2]])
            elif i[1] == 1:
                dq.append([i[0],i[2]])
            else:
                road_map[i[0]][i[1]] = min(i[2], road_map[i[0]][i[1]])
                road_map[i[1]][i[0]] = min(i[2], road_map[i[0]][i[1]])
                
    visited[1] = True
    
    while dq:
        e = dq.popleft()
        
        if e[1] <= K and visited[e[0]] == False:
            visited[e[0]] = True
            answer += 1
        
        for i in range(2,N+1):
            if road_map[e[0]][i] != 0 and e[1] + road_map[e[0]][i] <= K:
                dq.append([i, e[1] + road_map[e[0]][i]])
            
    return answer + 1

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],	3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],	4))

