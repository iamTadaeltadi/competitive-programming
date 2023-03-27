class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sett=set(nums)
        n=max(max(nums)+1,len(nums))
        for i in range(n):
            if i+1 not in sett:
                return i+1
        return n+1
        
            