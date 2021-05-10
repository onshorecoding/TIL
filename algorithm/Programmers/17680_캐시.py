from collections import deque


def solution(cacheSize, cities):
    answer = 0
    
    citie = [ x.lower() for x in cities]
    
    dq = deque([])
    len_dq = len(dq)
    
    city = deque(citie)
    
    if cacheSize == 0:
        return len(cities) * 5
    
    while city:

        c = city.popleft()
        print(dq)

        if c in dq:
            print("c in dq", c)
            dq.remove(c)
            dq.append(c)
            
            answer += 1
        else:

            if len(dq) >= cacheSize:
                k = dq.popleft()
                dq.append(c)
            else:
                dq.append(c)
            answer += 5
    
    return answer

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))