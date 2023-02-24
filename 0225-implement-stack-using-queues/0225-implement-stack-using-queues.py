class MyStack(object):

    def __init__(self):
        self.stack=[]
        

    def push(self, x):
        
        self.stack.append(x)
        """
        :type x: int
        :rtype: None
        """
    def pop(self):
        """
        :rtype: int
        """
        pop=self.stack.pop()
        return pop
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)>0:
            return self.stack[-1]
    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack)>0:
            return False
        return True
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()