class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        c=sorted(d.items(), key=lambda kv:(kv[1]))
        c=list(c)[::-1]
        res=[]
        for i in range(k):
            res.append(c[i][0])
        
        return res