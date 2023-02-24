class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in range(len(s)):
            if s[i]=="*" :
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
            
            
            
        