class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        sign=n&1
        n>>=1
        while n>0:
            if sign==1:
                if n&1!=0:
                    return False
                sign=0
            else:
                if n&1==0:
                    return False
                sign=1
                
            n>>=1
            
        return True
            