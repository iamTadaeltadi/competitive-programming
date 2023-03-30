class Solution:
    def findComplement(self, num: int) -> int:
        # print(bin(num))
        num=bin(num)
        res=list(num[2:])
        ans=[]
        for i in res:
            if i=="1":
                ans.append("0")
            else:
                ans.append("1")
        ans="0b"+"".join(ans)
        print(ans)
        return int(ans,2)
               
            
        