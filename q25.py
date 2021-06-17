
def validateStackSequences(pushed, popped):
    stack = []
        
    while True:
        if popped and stack and stack[-1]==popped[0]:
            stack.pop()
            popped.pop(0)
        elif pushed:
            stack.append(pushed.pop(0))
        else:
            break
    if not stack and not pushed and not popped:
        return True
    else:
        return False



pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validateStackSequences(pushed,popped))
