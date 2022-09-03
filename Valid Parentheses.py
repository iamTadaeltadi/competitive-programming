class Solution:
    def isValid(self, s: str) -> bool:
        stack=["Q"]
        for i in s:
            if i=="}"or i==")"or i=="]":
                if ord(i)-1 == ord(stack[-1]) or ord(i)-2== ord(stack[-1]): 
                    stack.pop()
                else:
                    return False
                    break
            else:stack.append(i)
        return len(stack)==1
