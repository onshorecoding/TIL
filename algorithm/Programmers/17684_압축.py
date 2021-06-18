import string
from collections import deque

def solution(msg):
    answer = []
    lzw_dict = {}
    idx = 1

    for i in list(string.ascii_uppercase):
        lzw_dict[i] = idx
        idx +=1

    print(lzw_dict)

    dq = deque(list(msg))
    check = ""
    while dq:
        e = dq.popleft()
        check += e
        if check in lzw_dict:
            if dq:
                continue
            else:
                answer.append(lzw_dict[check])
        else:
            ans =  lzw_dict[check[:-1]]
            answer.append(ans)

            lzw_dict[check]= idx
            idx+=1
            p = check[-1]
            dq.appendleft(p)
            check = ""
        print(dq)
        print(answer)
        print(lzw_dict)

solution("KAKAO")
solution("TOBEORNOTTOBEORTOBEORNOT")
solution("ABABABABABABABAB")