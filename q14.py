def removeKdigits(num, k):
    stack = []

    for n in num:
        while stack and k > 0 and stack[-1] > n:
            k -= 1
            stack.pop()
        stack.append(n)

    while stack and k > 0:
        stack.pop()
        k -= 1

    if not stack:
        return "0"

    return str(int("".join(stack)))
num = "1432219"
k = 3

print(removeKdigits(num,k))