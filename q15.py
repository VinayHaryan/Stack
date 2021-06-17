
def find132pattern(nums):
    n = len(nums)
    stack, third = [], float('-inf')
    for i in range(n-1,-1,-1):
        if nums[i]< third: 
            return True
        while stack and nums[i]>stack[-1]:
            third = stack.pop()
        stack.append(nums[i])
    return False

nums = [3,1,4,2]
print(find132pattern(nums))


