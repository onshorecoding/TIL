def check_correct(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            
        if cnt < 0:
            return False

    
    return True
        
def check_balance(p):
    return p.count('(') == p.count(')')

    
def solution(p):
    answer = ''
    u = []
    v = []
    
    if check_correct(p):
        return p
    
    for i in range(2, len(p)+1,2):
        if check_balance(p[:i]):
            u = p[:i]
            v = p[i:]
            break
            
    if check_correct(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + u[1:len(u)-1].replace('(', '0').replace(')', '(').replace('0', ')')