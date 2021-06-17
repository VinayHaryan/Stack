def scoreOfParentheses(S):
                
    stack = []
    for p in S:
        if p == '(':
            stack.append(0)
            
        else:
            score = 0
            while stack[-1]:       # case AB: score(A) + score(B)
                score += stack[-1]
                stack.pop()
            stack.pop() # pop 0 that corresponds to '('
            stack.append(2 * score if score else 1) # if score = 0 => case: "()" if score>0 => case "(A)"
              
    return sum(stack)

s =  "(()(()))"
print(scoreOfParentheses(s))
