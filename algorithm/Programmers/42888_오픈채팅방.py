def solution(record):
    answer = []
    nickname_dict = {}
    reverse_record = list(reversed(record))

    for log in reverse_record:
        log_set = list(map(str, log.split()))
        if len(log_set) == 3 and not log_set[1] in nickname_dict:
            nickname_dict[log_set[1]] = log_set[2]
    

    for data in record:
        data_set = list(map(str, data.split()))
        if data_set[0] == "Leave":
            word = nickname_dict[data_set[1]]+"님이 나갔습니다."
            answer.append(word)

        elif data_set[0] == "Enter":
            word = nickname_dict[data_set[1]]+"님이 들어왔습니다."
            answer.append(word)
        else:
            pass
        
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))