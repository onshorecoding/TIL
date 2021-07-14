T = int(input())

test_case = [list(map(list, input().split())) for _ in range(T)]

for case in test_case:
    n = int(case[0][0])
    text = ""
    for t in case[1]:
        text += t * n

    print(text)