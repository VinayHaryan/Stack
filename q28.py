def nextGreaterElements(nums):
    size = len(nums)
    nums+=nums
    res = [-1] * size
    stack = []
    for i in list(range(size))*2:
        while stack and (nums[stack[-1]] < nums[i]):
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res

a = [1,2,1]
print(nextGreaterElements(a))