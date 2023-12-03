class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            if nums[-1]<target:
                return len(nums)
            else:
                for i in nums:
                    if i>target:
                        return nums.index(i)