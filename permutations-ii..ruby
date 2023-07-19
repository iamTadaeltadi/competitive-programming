class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def back(nums,ans,temp):
            if len(nums)==0:
                ans.append(temp)
                return 
            for i in range(len(nums)):
                back(nums[:i]+nums[i+1:],ans,temp+[nums[i]])
        ans=[]
        back(nums,ans,[])
        return ans