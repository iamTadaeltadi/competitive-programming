class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l=0
        r=math.floor(math.sqrt(c))
        while l<=r:
            if l**2 +r**2<c:
                l+=1
            elif l**2 +r**2>c:
                r-=1
            else:
                return True
        return False
    
        