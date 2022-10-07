lass Solution(object):
    def longestMountain(self, nums):
        m=0
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                c=1
                j=i
                k=i
                while j>0 and nums[j]>nums[j-1]:
                    c+=1
                    j-=1
                print(c)
                while k<len(nums)-1 and nums[k]>nums[k+1]:
                    k+=1
                    c+=1
            else:
                continue 
            m=max(m,c)
        return m
                
                
                    
                
                
