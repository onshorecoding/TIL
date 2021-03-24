def solution(s):
    s = list(s)
    answer = 0
    ans = []

    for i in range(len(s)//2, 0, -1):
        cnt = 1

        if s[:i] == s[i:2*i]:
            check = s[:i]
            while check == s[i:2*i]:
                del s[:i]
                cnt += 1
            del s[:i]

        if cnt != 1:
            ans.append(str(cnt))
            ans = ans + check 

        while len(s) >0:
            print(i)
            if s[:i] == s[i:2*i]:
                print('loading self')
                cnt = 1
                check = s[:i]
                while check == s[i:2*i] and len(s)>0:
                    print('loading')
                    del s[:i]
                    cnt += 1    
                del s[:i]
                ans.append(str(cnt))
                ans = ans + check
            else:
                print('loading del')

                del s[0]
        break

    return ''.join(ans)


print(solution("abfdadad"))