n = int(input())
lst = [input() for _ in range(n)]
len_dct = {}
for l in lst:
    len_dct[l] = len(l)

sorted_lst = sorted(len_dct.items(), key = lambda x : (x[1],x[0]))

for letter in sorted_lst:
    print(letter[0])