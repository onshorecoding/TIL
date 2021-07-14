M, N = map(int, input().split())

mp = [list(input()) for _ in range(M)]

cnt = float("inf")

for i in range(0, M - 7):
    for j in range(0, N - 7):
        tmp = 0
        for k in range(8):
            for m in range(8):
                if (i + k + j + m) % 2:
                    if mp[i + k][j + m] != "W":
                        tmp += 1
                else:
                    if mp[i + k][j + m] != "B":
                        tmp += 1
                if tmp >= cnt:
                    break
            if tmp > cnt:
                break
        if tmp < cnt:
            cnt = tmp

        tmp = 0
        for k in range(8):
            for m in range(8):
                if (i + k + j + m) % 2:
                    if mp[i + k][j + m] != "B":
                        tmp += 1
                else:
                    if mp[i + k][j + m] != "W":
                        tmp += 1
                if tmp >= cnt:
                    break
            if tmp >= cnt:
                break

        if tmp < cnt:
            cnt = tmp

print(cnt)