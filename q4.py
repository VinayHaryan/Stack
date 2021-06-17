def buildArray(target,n):
    ans = []
    for i in range(1,target[-1]+1):
        if i in target:
            ans.append("Push")
        else:
            ans.append("Push")
            ans.append("Pop")
    return ans


t = [1,3]
n = 3
print(buildArray(t,n))