# n = int(input())
# time = [list(input().replace(":","").split(' ~ ')) for i in range(3)] 

# start_time = 0
# end_time = 2400 

# for t in time:
#     if int(t[0]) > start_time:
#         start_time = int(t[0])
#     if int(t[1]) < end_time:
#         end_time = int(t[1])

# if start_time >= end_time:
#     print("-1")
# else:
#     start_time =  str(start_time)
#     end_time =  str(end_time)
#     if len(start_time)<4 :
#         start_time = '0' + start_time
#     if len(end_time) < 4:
#         end_time = '0' + end_time
			
#     print(start_time[0:2], end="")
#     print(":", end= "")
#     print(start_time[2:],"~", end_time[0:2], end = "")
#     print( ":" , end ="")
#     print(end_time[2:])


# n = int(input())
# l = list(input())
# v = [0]* n

# v[0] = 1 

# if l[1] == '0':
#     v[1] = 0
# if l[1] == '1':
#     v[1] = 1

# for i in range(2, n):
#     if l[i] == '0':
#         v[i] = 0
#     else:
#         v[i] = v[i-1] + v[i-2]
    
# print(v[-1])

# n = int(input())
# m = [list(map(int, list(input()))) for _ in range(n)]

# def count_onebyone(m):
#     cnt = 0
#     for i in m:
#         cnt += sum(i)
#     return cnt

# def count_twobytwo(m):
#     cnt = 0
#     for i in range(n-1):
#         for j in range(n-1):
#             if m[i][j] == 1:
#                 if m[i+1][j] == 1 and m[i][j+1] == 1 and m[i+1][j+1] == 1:
#                     cnt += 1

#     return cnt

# print('total:', count_onebyone(m) + count_twobytwo(m))
# print('sizy:',count_onebyone(m))
# print('size[2]:',count_twobytwo(m))

# N, M = map(int, input().split())
# m = [list(map(int, input().split())) for _ in range(M)]
# mark = [[0]* N for _ in range(M)]

# for i in range(M):
# 	for j in range(N):
# 			if i == 0 and j == 0:
# 				mark[i][j] = m[i][j]
# 			elif i == 0 and j != 0:
# 				mark[i][j] = mark[i][j-1] + m[i][j]
# 			elif j == 0 and i != 0:
# 				mark[i][j] = mark[i-1][j] + m[i][j]
# 			else:
# 		 		mark[i][j] = max(mark[i-1][j], mark[i][j-1]) + m[i][j]
				
# print(mark[i][j])

# from collections import deque
# import copy

# def bfs(dq):
# 	global visited
# 	global rl
# 	v = copy.deepcopy(visited)
# 	r = copy.deepcopy(rl)
# 	ans = []
# 	while dq: 
# 		e = dq.popleft()
# 		x = e[0]
# 		y = e[1]  
# 		cnt = v[x][y] 
# 		mv = r[x][y]
		
# 		if x == M-1:
# 			ans.append([cnt,mv])
		
# 		if x + 1 < M and v[x+1][y] == 0 and m[x+1][y] == '.' :

# 			v[x+1][y] = cnt + 1
# 			r[x+1][y] = mv 
# 			dq.append([x+1, y])
# 		if y + 1 < N and v[x][y+1] == 0 and m[x][y+1] == '.':
			
# 			v[x][y+1] = cnt + 1
# 			r[x][y+1] = mv + 1
# 			dq.append([x, y+1])
		
# 		if 0 < x - 1 and v[x-1][y] == 0 and m[x-1][y] == '.':

# 			v[x-1][y] = cnt + 1
# 			r[x-1][y] = mv
# 			dq.append([x-1, y])
		
# 		if 0 < y - 1 and v[x][y-1] == 0 and m[x][y-1] == '.':
			
# 			v[x][y-1] = cnt + 1
# 			r[x][y-1] = mv + 1
# 			dq.append([x, y-1])
	
# 	return ans
	
	
# N, M = map(int,input().split())
# m = [list(input()) for _ in range(M)]
# visited = [[0]*N for _ in range(M)]
# rl = [[0]*N for _ in range(M)]

# start = deque([])

# for i in range(N):
# 	if m[0][i] == 'c':
# 		start.append([0,i])

# if bfs(start):
	
# else:
# 	print("-1")
	
# from collections import deque

# def dfs(dq, length):
# 	global ans
# 	next_dq = deque()
# 	b = False
# 	dx = [0,1,1]
# 	dy = [1,0,1]

# 	while dq:
# 		e = dq.popleft()
# 		x = e[0]
# 		y = e[1]
		
# 		for i in range(3):
# 			new_x = x + dx[i]
# 			new_y = y + dy[i]
		
# 			if 0 <= new_x < n and 0 <= new_y < n:
# 				if m[new_x][new_x] != 1:
# 					return None
# 				else:
# 					next_dq.append([new_x, new_y])

#     ans.append(length+1)
#     return dfs(next_dq, length+1)

# n = int(input())
# m = [list(map(int, list(input()))) for _ in range(n)]

# a = [[]*n for _ in range(n)]
# ans = []
# start = deque()

# for i in range(n):
# 	for j in range(n):
# 		if m[i][j] == 1:
# 			dfs(deque([i,j]), 1)

# print(ans)


# from collections import deque

# def dfs(dq, length):
# 	global ans
# 	b = False
# 	next_dq = deque([])
# 	dx = [0,1,1]
# 	dy = [1,0,1]
	
# 	ans.append(length)
# 	print(dq, length)
# 	while dq:
# 		e = dq.popleft()
# 		x = e[0]
# 		y = e[1]

# 		for i in range(3):
# 			new_x = x + dx[i]
# 			new_y = y + dy[i]
		
# 			if 0 <= new_x < n and 0 <= new_y < n:
# 				if m[new_x][new_x] == 1:
# 					next_dq.append([new_x, new_y])
# 				else:
# 					return
# 	return dfs(next_dq, length+1)


# n = int(input())
# m = [list(map(int, list(input()))) for _ in range(n)]

# a = [[]*n for _ in range(n)]
# ans = []

# for i in range(n):
# 	for j in range(n):
# 		if m[i][j] == 1:
# 			dfs(deque([[i,j]]), 1)
			
# print(ans)

from itertools import combinations


def solution(number, k):
    length = len(number)
    answer = 0

    number = list(number)

    l_num  = [ i for i in range(length)]
    l_list = list(combinations(l_num, k))

    for i in l_list:
        check = number[:]
        for j in range(k):
            del check[i[j] - j]
        point = int(''.join(check))
        if point > answer:
            answer = point

    return answer

