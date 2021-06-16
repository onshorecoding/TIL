def solution(numbers, hand):
    answer = ''
    state = [10,12]
    
    if hand == "right" :
        personal_hand = "R"
    if hand == "left" :
        personal_hand = "L"

    for point in numbers:
        
        if point == 1 or point == 4 or point == 7:
            answer += "L"
            state[0] = point
        if point == 3 or point == 6 or point == 9:
            answer += "R"
            state[1] = point
        
        if point == 2 or point == 5 or point == 8 or point== 0:
            if state[1] + state[0] == point*2:
                if personal_hand == "R":
                    answer += "R"
                    state[1] = point
                else:
                    answer += "L"
                    state[0] = point

            elif state[1]-state[0] == 2:
                if personal_hand == "R":
                    answer += "R"
                    state[1] = point
                else:
                    answer += "L"
                    state[0] = point
                    
            else :
                if point ==0 :
                    if point - state[0] < state[1] - point:
                        answer += "R"
                        state[1] = point
                    else:
                        answer += "L"
                        state[0] = point
                else:
                    if point - state[0] > state[1] - point:
                        answer += "R"
                        state[1] = point
                    else:
                        answer += "L"
                        state[0] = point

        
    return answer