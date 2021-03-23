from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    
    while truck_weights:
        bridge.popleft()
        
        if sum(bridge) + truck_weights[0] <= weight:
            e = truck_weights.popleft()
            bridge.append(e)
        else: 
            bridge.append(0)
        answer += 1
        
    return answer + bridge_length