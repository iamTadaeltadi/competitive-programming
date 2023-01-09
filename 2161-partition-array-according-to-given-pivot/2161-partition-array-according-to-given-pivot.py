class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        before=[]
        after=[]
        between=[]
        for i in nums:
            if i<pivot:
                before.append(i)
            elif  i>pivot:
                after.append(i)
            else:
                between.append(i)
        return before+between+after
        
        
        