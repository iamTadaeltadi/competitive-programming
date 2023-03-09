class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 1 and s[-1].isdigit():
            return ''
        
        stack=[]
        for i in s:
            
            if i!="]":
                stack.append(i)
            else:
                val=""
                while stack and stack[-1]!='[':
                    val = stack.pop() + val
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * val)
        
                
            
                
                
        return ''.join(stack)
        