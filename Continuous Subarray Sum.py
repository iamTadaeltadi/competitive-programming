class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        r={0:-1}
        t=0
        for i,j in enumerate(nums):
            t+=j
            re=t%k
            if re not in r:
                r[re]=i
            elif i -r[re]>1:
                return True
        return False
            
        
