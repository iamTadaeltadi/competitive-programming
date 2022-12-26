class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=Counter(nums)
        c=0
        for i in count:
            c+=(count[i])*(count[i]-1)/2
        return c
            

        
        