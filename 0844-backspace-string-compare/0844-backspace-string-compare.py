class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1=[]
        stack2=[]
        for i in s:
            if stack1 and i=="#":
                stack1.pop()
            if i!='#':
                stack1.append(i)
        for i in t:
            if stack2 and i=="#":
                    stack2.pop()
            if i!='#':
                stack2.append(i)
        return stack1==stack2
    
            
            
        