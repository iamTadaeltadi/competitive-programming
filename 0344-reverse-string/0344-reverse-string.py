class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.list1=s
        result = self.rec(0, len(s)-1)
        
        return result
         
        
    def rec(self,l,r):
        if l>r:
            return 
        self.list1[l],self.list1[r]=self.list1[r],self.list1[l]
        l+=1
        r-=1
        return self.rec(l,r)
            