class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            
            while i+1!=nums[i] and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i in range(len(nums)):
            if i+1!=nums[i]:
                res.append(i+1)
        return res