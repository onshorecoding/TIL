def solution(n):
    ans = 1
    
#     value = [0]*(n+1)

#     for i in range(1, n+1):
#         if i%2 == 0:
#             value[i] = value[i//2]
#         else:
#             value[i] = value[i-1]+1
    
#     return value[n]

    while n != 1:
        if n % 2 != 0:
            n = n-1
            ans += 1
        else: 
            n = n/2
    
    return ans
 

    return bin(n)[2:].count('1')




    def mergeSort(a):
        if len(a) > 1: 
        mid = len(a)//2 
        la, ra = a[:mid], a[mid:] 
        mergeSort(la) 
        mergeSort(ra) 
        li, ri, i = 0, 0, 0 
        while li < len(la) and ri < len(ra):
            if la[li] < ra[ri]: 
                a[i] = la[li] 
                li += 1 
            else: 
                a[i] = ra[ri] 
                ri += 1
            i += 1 
        a[i:] = la[li:] if li != len(la) else ra[ri:]