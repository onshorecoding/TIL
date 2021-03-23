from collections import deque

def solution(board, moves):
    answer = 0
    dq = deque([])
    
    for i in moves:
        for k in board:
            if k[i-1] != 0:
                d = k[i-1]
                k[i-1] = 0
                if dq:
                    if dq[0] == d:
                        dq.popleft()
                        answer += 2
                    else:
                        dq.appendleft(d)     
                else:
                    dq.append(d)
                break
    
    return answer
                