class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={ i:0 for i in nums}
        for i in nums:
            d[i]+=1
        dd=list(sorted(d.values()))[::-1]
        t=0
        print(dd)
        for i in dd:
            for j in range(1,i):
                t+=(j)
        return t
                
