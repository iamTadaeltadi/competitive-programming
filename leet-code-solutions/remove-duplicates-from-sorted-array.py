class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        r=1
        while r<len(nums):
            if nums[r] in nums[:l]:
                r+=1
            elif nums[r] not in nums[:l]:
                nums[r],nums[l]=nums[l],nums[r]
                l+=1
                r+=1
        return l
        