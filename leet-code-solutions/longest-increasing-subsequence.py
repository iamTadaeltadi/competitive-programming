class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp =[1 for i in range(len(nums))]
        

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):

                if nums[i] <nums[j]:
                    dp[i] =max(1+dp[j],dp[i])
        return (max(dp))



