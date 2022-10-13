class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        x=[]
        c=0
        for i in range(len(pushed)+1):
            while x and x[-1]==popped[c]:
                x.pop()
                c+=1
            if i!=len(pushed):
                x.append(pushed[i])
        if not x:return True
        return False
