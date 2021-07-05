n =  int(input())

lsted = []

for _ in range(n):
    serial = input()
    l = len(serial)
    s = 0
    for code in serial:
        if code.isdigit():
           s += int(code)
           
    lsted.append((serial,l,s))

sorted_lst = sorted(lsted, key= lambda x : (x[1],x[2],x[0]))
for serial in sorted_lst:
    print(serial[0])