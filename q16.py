
def sumSubarrayMins(arr):
    stack = []
    output = 0
        
    for i in range(len(arr)):
        while len(stack) and arr[stack[-1][0]] >= arr[i]:
            stack.pop()
                
        sum_ = 0

        if len(stack):
            sum_ += stack[-1][1] + (i - stack[-1][0])*arr[i]
        else:
            sum_ += arr[i] * (i + 1)

        stack.append((i, sum_,))
        output = (output + sum_) % (10**9 + 7)
            
    return output

arr = [3,1,2,4]
print(sumSubarrayMins(arr))
