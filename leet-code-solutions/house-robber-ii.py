class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <=3:
            return max(nums)

        dp = [nums[0],max(nums[1],nums[0])]

        
        for i in range(2,len(nums)-1):
            dp.append(max(dp[-1],dp[-2]+nums[i]))

        print(dp)

        nums= nums[1:]
        
        dp2 = []

        dp2 = [nums[0],max(nums[1],nums[0])]


        
        for i in range(2,len(nums)):
            dp2.append(max(dp2[-1],dp2[-2]+nums[i]))

        print(dp2)
        return max(dp2[-1],dp[-1])
        