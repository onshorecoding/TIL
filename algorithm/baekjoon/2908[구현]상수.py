lst = list(map(str, input().split()))
answer = 0
for n in lst:
    if int(n[::-1]) > answer:
        answer = int(n[::-1]) 

print(answer)