from collections import deque

case = int(input())


def bfs(l, start, end):
    d = [(-2, 1), (-2, -1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    start.append(0)
    dq = deque([start])
    visited = [[False] * l for _ in range(l)]
    visited[start[0]][start[1]] = True
    while dq:
        e = dq.popleft()

        for i in range(8):
            nx = e[0] + d[i][0]
            ny = e[1] + d[i][1]
            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    cnt = e[2] + 1
                    if [nx, ny] == end:
                        return cnt
                    else:
                        dq.append([nx, ny, cnt])
    return 0


answer = []

for i in range(case):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    ans = bfs(l, start, end)
    answer.append(str(ans))

print("\n".join(answer))
