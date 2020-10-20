class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []   # array for stack init
        self.min = float("inf")   # initialize current min to infinity

    def push(self, x: int) -> None:
        if x < self.min:        # while pushing, we push it as tupe (x,y) -- x is actual value, and y represents current
                                # min in stack
            self.min = x
        self.data.append((x,self.min)) 
        

    def pop(self) -> None:
        self.data.pop()           
        if self.data:
            self.min = self.data[-1][1]     # after popping change current min value to y in (x,y) of current top element
                                            # of stack
        else:
            self.min = float("inf")            # if stack is empty change curr min to infinity back

    def top(self) -> int:
        return self.data[-1][0]              # return first index of top element (x,y) on stack

    def getMin(self) -> int:
        return self.data[-1][1]              # return second index of top element (x,y) on stack


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()