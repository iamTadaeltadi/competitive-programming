class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!=")":
                stack.append(i)
            else:
                t=[]
                while stack[-1]!="(":
                    t.append(stack.pop())
                stack.pop()
                stack+=t
                
        return "".join(stack)
                
                
        
