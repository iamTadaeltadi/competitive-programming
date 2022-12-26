class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count=Counter(t)
        
        count1=Counter(s)
        
        for i in count:
            
            if i in count1 and count1[i]==count[i]:
                pass
            else:
                
                return i
