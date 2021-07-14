T = int(input())
answer = []

for i in range(T):
    l = int(input())
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c1[1] += c2[0]
    c2[1] += c1[0]
    for j in range(2, l):
        c1[j] += max(c2[j - 1], c2[j - 2])
        c2[j] += max(c1[j - 1], c1[j - 2])

    answer.append(str(max(c1[-1], c2[-1])))

print("\n".join(answer))
