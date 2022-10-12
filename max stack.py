lass MinStack:

    def __init__(self):
        self.s1=[]
        self.s2=[]
    def push(self, val: int) -> None:
        if len(self.s1)==0:
            self.s2.append(val)
        else:
            if self.s2[-1]>=val:
                self.s2.append(val)
        self.s1.append(val)
    def pop(self) -> None:
        x=self.s1[-1]
        self.s1.pop()
        if x==self.s2[-1]:
            self.s2.pop()
        return x
    def top(self) -> int:
        return self.s1[-1]
    def getMin(self) -> int:
        return self.s2[-1]
        
        
