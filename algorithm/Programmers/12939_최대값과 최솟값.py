def solution(s):
    answer = ''
    s_lst = list(map(int, s.split()))
    
    answer = [str(min(s_lst)), str(max(s_lst))]
    return ' '.join(answer)


print(solution("-1 -2 -3 -4"))