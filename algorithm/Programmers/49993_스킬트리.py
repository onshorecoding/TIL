from collections import deque

# def solution(skill, skill_trees):

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

answer = [1] * len(skill_trees)
skill = list(skill)


answer = [1] * len(skill_trees)
skill = list(skill)
    
for i in range(len(skill_trees)):
    trees = list(skill_trees[i])
    for j in trees:
        if j not in skill:
            trees.remove(j)
    skill_trees[i] = trees      

for i in range(len(skill_trees)):
    dq = deque(skill_trees[i])
    cnt = 0
    
    while dq:
        e = dq.popleft()
        print(e)
        print(skill[cnt])
        if skill[cnt] != e:
            answer[i] = 0
            break
        else:
            cnt += 1
print(answer)
    
