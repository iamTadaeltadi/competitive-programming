class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        x=[]
        if len(num)==k:return str(0)
        for i in range(len(num)):
            while k and x  and x[-1]>num[i]:
                x.pop()
                k-=1
            x.append(num[i])
        n=len(x)
        return str(int("".join(x[:n-k])))
