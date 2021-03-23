from itertools import combinations

def solution(numbers):
    answer = []
    combi = list(combinations(numbers, 2))
    
    for lst in combi:
        s = sum(lst)
        if s not in answer:
            answer.append(s)
        
    answer.sort()
    
    return answer