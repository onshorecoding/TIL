from collections import deque

def is_same(mp):
    total_cnt = len(mp)^2
    total_item = [item for line in mp for item in line]

    if sum(total_item) == total_cnt:
        return 1
    elif sum(total_item) == 0:
        return 0
    else:
        return False

def devide_map(mp):
    arr_len = len(mp)
    dev_point = arr_len // 2

    map1 = []
    map2 = []
    map3 = []
    map4 = []

    for i in range(arr_len):
        line1 = []
        line2 = []
        line3 = []
        line4 = []
        for j in range(arr_len):
            if i < dev_point and j < dev_point:
                line1.append(mp[i][j])
            if i < dev_point and j >= dev_point:
                line2.append(mp[i][j])
            if i >= dev_point and j < dev_point:
                line3.append(mp[i][j])
            if i >= dev_point and j >= dev_point:
                line4.append(mp[i][j])
        if i < dev_point:
            map1.append(line1)
            map2.append(line2)
        else:
            map3.append(line3)
            map4.append(line4)

    return map1, map2, map3, map4


def solution(arr):
    answer = [0,0]

    dq = deque([arr])

    while dq:
        block = dq.popleft()
        if len(block) == 1:
            continue
        else:
            m1, m2, m3, m4 = devide_map(block)

   


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
