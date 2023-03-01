class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        max_value=float("-inf")
        tot=sum(nums[:k-1])
        
        for r in range(k-1,len(nums)):
            tot+=nums[r]
            max_value=max(max_value,tot)
            print(max_value)
            tot-=nums[l]
            l+=1
        return max_value/k
            
            
            