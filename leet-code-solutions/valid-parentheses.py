class Solution:
    def isValid(self, s: str) -> bool:
        o={"(","[","{"}
        d={"(":")","[":"]","{":"}"}
        x=[]
        for i in s:
            if i in o:
                x.append(i)
            else:
                if not x:return False
                if d[x.pop()]!= i:
                    return False
        if x:
            return False
        return True
                    