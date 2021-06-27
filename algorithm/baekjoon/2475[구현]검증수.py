lst = list(map(int, input().split()))

num = 0
for n in lst:
    num += n * n

print(num % 10)
