def check_long_pattern(word: str):
    for i in range(10, 0, -1):
        l = len(word) // i * i


n = int(input())
for i in (1, n + 1):
    pass