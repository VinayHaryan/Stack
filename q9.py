
def nextGreaterElement(nums1,nums2):
    # nums1 is a subset of nums2
    result = []
        
    for i, n in list(enumerate(nums1)):
        ind = nums2.index(n)
        flag = False
        for i in range(ind, len(nums2)):
            if nums2[i] > n:
                result.append(nums2[i])
                flag = True
                break
        if not flag:
            result.append('-1')
                
    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1,nums2))