from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
		
		# python natively support double-ended queue
        self.queue = deque()
        
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        
		# push new element into queue's tail
        self.queue.append(x)
        
        # make new element on the head position by rotation
        for _ in range(len(self.queue)-1):
            self.queue.append( self.queue.popleft() )
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        
		# pop head element of queue
        return self.queue.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        
		# return head element of queue
        return self.queue[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        
        return (not self.queue)

n= MyStack()
print(n.push(1))
print(n.push(2))
print(n.top()) # return 2
print(n.pop()) # return 2
print(n.empty())s # return False
