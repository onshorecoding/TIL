from collections import deque

def solution(arr, divisor):
    answer = []
    
    arr = deque(arr)
    
    while arr:
        e = arr.popleft()
        
        if e % divisor == 0:
            answer.append(e)
    
    answer.sort()
    if not answer:
        answer.append(-1)
    
    return answer