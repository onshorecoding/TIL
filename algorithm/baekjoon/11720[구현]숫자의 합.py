from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES


n = int(input())
N = list(input())

answer = 0
for n in N:
    answer += int(n)    

print(answer)
