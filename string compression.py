class Solution:
    def compress(self, nums: List[str]) -> int:
    
        left,i=0,0
        while i<len(nums):
            x,y=nums[i],1
            while i+1<len(nums) and x==nums[i+1]:
                y+=1
                i+=1
            nums[left]=x
            if y>1:
                nums[left+1:left+1+ len(str(y))]=str(y)
                left+=len(str(y))
            left+=1
            i+=1
        return left
