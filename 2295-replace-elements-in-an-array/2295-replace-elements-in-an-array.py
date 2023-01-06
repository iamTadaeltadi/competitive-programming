class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        dd={}
        d={}
        for i in range(len(nums)):
            dd[nums[i]]=i
        for i,j in operations:
            nums[dd[i]]=j
            dd[j]=dd[i]
            del dd[i]
        return nums
        