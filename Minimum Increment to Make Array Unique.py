class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        s=set()
        x=[]
        c=0
        for i in range(len(nums)):
            if nums[i] in s:
                c+=abs(x[-1]-nums[i])+1
                s.add(nums[i]+abs(x[-1]-nums[i])+1)
                x.append(nums[i]+abs(x[-1]-nums[i])+1)
            else:
                s.add(nums[i])
                x.append(nums[i])
        return c
