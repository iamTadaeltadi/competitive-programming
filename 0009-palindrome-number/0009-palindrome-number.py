class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        c=x
        y=0
        while x>0:
            y = y*10 + x%10
            x//=10
        
        return c==y
            
        
        
        