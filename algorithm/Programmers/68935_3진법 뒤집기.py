def solution(n):
    answer = []
    while True:
        n, rest = divmod(n, 3)
        answer.append(rest)
        
        if n == 0:
            break
    
    answer = sum([num * 3**idx for idx, num in enumerate(reversed(answer))])
    
    return answer