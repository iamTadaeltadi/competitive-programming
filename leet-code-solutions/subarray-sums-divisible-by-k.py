class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        x=list(accumulate(nums))
        print(x)
        d={0:1}
        c=0
        for i in x:
            if i%k not in d:
                d[i%k]=1
            else:
                c+= d[i%k]
                d[i%k]+=1
        return c
                

