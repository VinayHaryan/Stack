
import collections
def removeDuplicateLetters(s):
    countMap = collections.defaultdict(int)
    stack = []
    selected = set()

    for c in s:
        countMap[c] += 1

    for c in s:
        countMap[c] -= 1
        if c not in selected:
            while stack and countMap[stack[-1]] > 0 and stack[-1] > c:
                selected.remove(stack.pop())
                    
            stack.append(c)
            selected.add(c)
                
    return "".join(stack)


s = "cbacdcbc"
print(removeDuplicateLetters(s))
