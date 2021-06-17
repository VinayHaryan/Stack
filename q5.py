
def removeDuplicates(S):
    if not S:
        return S
    res = [S[0]]
    for curr in S[1:]:            
        if res and curr == res[-1]:
            res.pop()
        else:
            res.append(curr)
    res = ''.join(res)                
    return res

input = "abbaca"
print(removeDuplicates(input))


