class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        

        def backtrack(i,curr,c,stack):

            if c>n or c< -1*(n):
                return 

            if i ==n*2:
                print(curr)
                if not stack:
                    ans.append(curr)
                return
            
            if stack and stack[-1]=="(":
                backtrack(i+1,curr +")",c+1,stack[:-1])
            else:
                backtrack(i+1,curr +")",c+1,stack+")")

            backtrack(i+1,curr +"(",c-1,stack+"(")
           

        backtrack(0,"",0,'')
        return ans


