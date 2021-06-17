def minAddToMakeValid(S):
    s = []
    for i in S:
        if i == '(':
            s.append(i)
        else:
            if s and s[-1] == '(':
                s.pop()
            else:
                s.append(i)
    return len(s)

s= "((("
print(minAddToMakeValid(s))
