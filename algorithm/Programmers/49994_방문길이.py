def solution(dirs):
    answer = 0
    mp = [[[0, 0, 0, 0] for i in range(11)] for j in range(11)]
    pointer = [5, 5]

    for dir in list(dirs):
        x = pointer[0]
        y = pointer[1]

        if dir == "U":
            if 0 <= x < 11 and 0 <= y + 1 < 11:
                mp[x][y][0] = 1
                pointer = [x, y + 1]
                mp[x][y][1] = 1
                
        if dir == "D":
            if 0 <= x < 11 and 0 <= y - 1 < 11:
                mp[x][y][1] = 1
                pointer = [x, y - 1]
                mp[x][y][0] = 1
        if dir == "R":
            if 0 <= x + 1 < 11 and 0 <= y < 11:
                mp[x][y][2] = 1
                pointer = [x + 1, y]
                mp[x][y][3] = 1
        if dir == "L":
            if 0 <= x - 1 < 11 and 0 <= y < 11:
                mp[x][y][3] = 1
                pointer = [x -1 , y]
                mp[x][y][2] = 1

    for i in range(11):
        for j in range(11):
            for k in range(4):
                answer += mp[i][j][k]

    return int(answer / 2)

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))

# def solution(dirs):
#     dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
#     d = {"U": 0, "L":1, "D":2, "R": 3}

#     visited = set()
#     answer = 0
#     x, y = 0, 0
#     for dir in dirs:
#         i = d[dir]
#         nx, ny = x + dxs[i], y + dys[i]
#         if nx < -5 or nx > 5 or ny < -5 or ny > 5:
#             continue
#         if (x, y, nx, ny) not in visited:
#             visited.add((x, y, nx, ny))
#             visited.add((nx, ny, x, y)) # 길은 '양방향' 임을 빼먹으면 안됨!
#             answer += 1
#         x, y = nx, ny

#     return answer