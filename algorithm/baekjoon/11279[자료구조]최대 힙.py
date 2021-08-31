from sys import stdin
import heapq

input = stdin.readline
n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if not num:
        if heap:
            print(heapq.heappop(heap) * (-1))

        else:
            print(0)
    else:
        heapq.heappush(heap, num * (-1))
