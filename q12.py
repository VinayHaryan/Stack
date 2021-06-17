def makeGood(s):
    stack = list()
    for c in s:
        if stack and stack[-1].lower() == c.lower():
            if stack[-1] == c:
                stack.append(c)
            else:
                stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)

s = "leEeetcode"
print(makeGood(s))
