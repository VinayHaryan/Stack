def backspaceCompare(S, T):
        
    ans = ''
    ans_2 = ''
    for i in S:
        if i == '#':
            ans = ans[:-1]
        else:
            ans += i
        
    for i in T:
        if i == '#':
            ans_2 = ans_2[:-1]
        else:
            ans_2 += i
    return ans == ans_2


s = "ab#c"
t = "ad#c"
print(backspaceCompare(s,t))
