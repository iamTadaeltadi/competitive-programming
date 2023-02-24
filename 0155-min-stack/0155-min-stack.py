class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.m=float("inf")
        
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.stack:
            self.stack.append([val,min(self.stack[-1][1],val)])
        else:
            self.stack.append([val,val])
    def pop(self): 
        """
        :rtype: None
        """
        if len(self.stack)>0:
            pop=self.stack.pop()[0]
            return pop
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)>0:
            return self.stack[-1][0]
    def getMin(self):
        """
        :rtype: int
        """
        return  self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()