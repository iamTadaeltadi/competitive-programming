class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = [[s[0],1]]

        for i in range(1,len(s)):

            if stack and stack[-1][0]==s[i] and stack[-1][1]>=k-1:
                while stack and stack[-1][0]==s[i] :
                    stack.pop()


            elif  stack:
                stack.append([s[i],stack[-1][1]+1 if stack[-1][0] == s[i] else 1 ])
            else:
                stack.append([s[i],1])
        print(stack)

        return "".join([i[0] for i in stack])