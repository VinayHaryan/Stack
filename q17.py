
def longestWPI(hours):
    Sum, ans = 0, 0
    cache = {}
    for i, n in enumerate(hours):
        Sum = Sum + 1 if n > 8 else Sum - 1
        if Sum > 0: ans = i + 1
        if Sum-1 in cache:
            ans = max(ans, i - cache[Sum-1])
        cache.setdefault(Sum, i)
    return ans

hours = [9,9,6,0,6,6,9]
print(longestWPI(hours))
