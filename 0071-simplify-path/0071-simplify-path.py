class Solution(object):
    def simplifyPath(self, path):
        x=path.split("/")
        stack=[]
        for i in x:
            if stack and i=="..":
                stack.pop()
            if not (i=="" or i==".." or i=="."):
                stack.append(i)
        return "/" + "/".join(stack)