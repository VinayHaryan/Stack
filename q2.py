class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []
        self.m = []

        
    def push(self, x: int):
        self.a.append(x)
        m = self.m
        m.append(x if  not m else min(x,m[-1]))
        
    def pop(self):
        self.a.pop()
        self.m.pop()

    def top(self):
        return self.a[-1]
        
    def getMin(self):
        return self.m[-1]

obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.getMin())
print(obj.pop())
print(obj.top()) 
print(obj.getMin())


# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()