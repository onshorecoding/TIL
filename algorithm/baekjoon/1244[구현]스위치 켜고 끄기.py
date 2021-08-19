num = int(input())
lst = list(map(int, input().split()))
n = int(input())
action_lst = [tuple(map(int, input().split())) for _ in range(n)]

for gender, x in action_lst:
    if gender == 1:
        for idx, switch in enumerate(lst):
            if not (idx + 1) % x:
                lst[idx] = 1 if lst[idx] == 0 else 0
    else:
        x -= 1
        idx = 0
        while x - idx >= 0 and x + idx < num:
            if lst[x - idx] == lst[x + idx]:
                lst[x - idx] = 1 if lst[x - idx] == 0 else 0
                lst[x + idx] = lst[x - idx]
            else:
                break
            idx += 1

for idx, switch in enumerate(lst, start=1):
    print(switch, end=" ")
    if not idx % 20:
        print()
