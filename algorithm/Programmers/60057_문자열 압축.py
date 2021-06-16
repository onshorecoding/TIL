def solution(s):
    str_len = len(s)
    ans = [str_len]

    for size in range(str_len // 2, 0, -1):
        unit_lst = [s[i : i + size] for i in range(0, str_len, size)]
        stack = [[unit_lst[0], 1]]

        for unit in unit_lst[1:]:
            if stack[-1][0] != unit:
                stack.append([unit, 1])
            else:
                stack[-1][1] += 1
        
        wrd = ("").join([str(cnt) + w if cnt > 1 else w for w, cnt in stack])
        ans.append(len(wrd))

    return min(ans)


print(solution("aabbaccc"))