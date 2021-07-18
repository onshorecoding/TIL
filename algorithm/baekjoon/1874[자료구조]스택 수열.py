n = int(input())
check = [int(input()) for _ in range(n)]

cnt = 0
dq = []
ans = []
able = True

for num in check:
    while cnt < num:
        cnt += 1
        dq.append(cnt)
        ans.append("+")

    if dq[-1] == num:
        dq.pop()
        ans.append("-")
    else:
        able = False
        break

if able:
    print("\n".join(ans))
else:
    print("NO")
