from collections import deque

def solution(arr):
    answer = []
    
    arr = deque(arr)
    
    while arr:
        e = arr.popleft()
        if not answer:
            answer.append(e)
        elif e != answer[-1]:
            answer.append(e)
        
    return answer