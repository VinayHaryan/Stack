
def reverseParentheses(s):
    stack = []
    for i in range(len(s)):
        if s[i]!=')':
            stack.append(s[i])
        else:
            stri = ''
            while stack and stack[-1]!='(':
                stri += stack.pop()
            stack.pop()
            for st in stri:
                stack.append(st)
    return ''.join(stack)

s = '(u(love)i)'
print(reverseParentheses(s))