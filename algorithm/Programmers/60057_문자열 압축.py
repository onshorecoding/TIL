def solution(s):
    answer = 0
    l = len(s)
    ans = []
      
    for i in range(l//2, 2, -1):
        cnt = 0
        while l > 2*i:
            print("loading", s)
            if s[:i] == s[i:2*i]:
                ans = s[:i]
                s = s[i:2*i]
                cnt += 1
            print(ans)
        if cnt != 0:
            break      
            
    return ans

solution("aabbaccc")