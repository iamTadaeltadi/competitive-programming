class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def subset(i,curr):
            if i==len(nums):
                return 
            for i in range(i,len(nums)):
                curr.append(nums[i])
                res.append(curr.copy())
                subset(i+1,curr)
                curr.pop()
        subset(0,[])
        res. insert(0, [])
        return res
        