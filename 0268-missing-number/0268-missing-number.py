class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums+=[-1]
        count=0
        for index in range(len(nums)):
            count=0
            while (nums[index]!=index and nums[index]!=-1)  and count<len(nums):
                nums[nums[index]],nums[index]=nums[index],nums[nums[index]]
                count+=1
        return nums.index(-1)