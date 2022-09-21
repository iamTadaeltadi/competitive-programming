class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=1
        c=0
        for i in nums:
            if i==0:
                c+=1       
            else:total*=i
        for i in range(len(nums)):
            if nums[i]==0 and c==1:
                nums[i]=total
            elif c>=2 and nums[i]==0:
                nums[i]=0
            elif nums[i]!=0 and c==0:
                nums[i]=(total)/nums[i]
            elif nums[i]!=0 and c!=0:
                nums[i]=0
            
        return map(int,nums)
            
    
            
            
        
