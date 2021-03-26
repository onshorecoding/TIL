from collections import deque

def solution(n, lost, reserve):
    answer = n
    
    lost.sort()
    reserve.sort()
    
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    
    cnt =0 
    
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i-1)
            cnt += 1
            continue
            print(i)
            
        if i + 1 in reserve:
            reserve.remove(i+1)
            lost.remove(i)
            cnt += 1
            print(i)
            
    return answer - len(lost) + cnt

print(solution(5,[2, 4],[3]))