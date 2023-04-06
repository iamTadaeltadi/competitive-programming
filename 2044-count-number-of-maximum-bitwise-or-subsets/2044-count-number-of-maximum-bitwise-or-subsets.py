class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res=[]
        ans=[]
        def count(index,curr):
            res.append(curr.copy())
            if curr:
                orValue=0
                for i in curr:
                    orValue|=i
                ans.append(orValue)
                
                    
                    
            for i in range(index,len(nums)):
                curr.append(nums[i])
                count(i+1,curr)
                curr.pop()
        count(0,[])
        return ans.count(max(ans))
                
                    