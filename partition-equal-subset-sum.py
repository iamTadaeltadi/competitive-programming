class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)

        if total_sum%2 !=0:
            return False
        @cache
        def dp(index,sum1):
            if sum1 == total_sum//2 :
                return True

            if index >=len(nums):
                return False
            

            return dp(index+1,sum1+nums[index]) or dp(index+1,sum1)
        
        return dp(0,0)