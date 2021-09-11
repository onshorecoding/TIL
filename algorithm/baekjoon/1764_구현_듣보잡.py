from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
hear = [input().rstrip() for _ in range(n)]
look = [input().rstrip() for _ in range(m)]

ans = sorted(list(set(hear) & set(look)))


print(len(ans))
print("\n".join(ans))