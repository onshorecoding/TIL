m = list(map(int, input().split()))

def soultion():
    if m[0] > m[1]:
        answer = "descending"
    elif m[0] <  m [1]:
        answer =  "ascending"
    else: 
        return "mixed"

    for i in range(1,len(m)):
        if m[i-1] > m[i]:
            if answer != "descending":
                return "mixed"
        elif m[i-1] <  m[i]:
            if answer != "ascending":
                return "mixed"
        else: 
            return "mixed"
    return answer

print(soultion())