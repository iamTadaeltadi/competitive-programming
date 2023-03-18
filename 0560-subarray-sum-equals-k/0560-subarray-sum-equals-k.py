class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counterOfPrefix=defaultdict(int)
        counterOfPrefix[0]+=1
        res=0
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=(nums[i])
            
            if prefix_sum-k in counterOfPrefix:
                res+=counterOfPrefix[prefix_sum-k]
                
            counterOfPrefix[prefix_sum]+=1
            
        return res