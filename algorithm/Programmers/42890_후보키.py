# 미해결

from collections import Counter
from itertools import combinations

def solution(relation):
    answer = 0
    
    len_column = len(relation[0])
    len_row = len(relation)
    
    data = []
    
    for i in range(len_column):
        data_column = []
        for column in relation:
            data_column.append(column[i])
            
        data.append(data_column)
    

    combination_num = 1

    while True:

        if len(data) < combination_num:
            break
        else:
            data_set = list(combinations(data, combination_num))

            for col in data_set:
                for i in col:
                    print(Counter(i))

        combination_num += 1
    
    
    
    return data

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))