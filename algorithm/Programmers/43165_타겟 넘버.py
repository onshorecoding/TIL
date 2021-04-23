from collections import deque

def dfs(dq, equ, target):
    global answer

    if len(dq) != 0:
        e = dq.popleft()
        dfs(dq, equ - e, target)
        dfs(dq, equ + e, target)
        dq.appendleft(e)


    else:
        print(equ, target)
        if equ == target:
            answer += 1
            return answer

        
def solution(numbers, target):
    global answer
    
    dq = deque(numbers)
    
    dfs(dq, 0, target)
    
    return answer
    
answer = 0
print(solution([1,1,1,1,1], 3))