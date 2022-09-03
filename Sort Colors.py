def sortColors(self, nums):
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        d={0:0,1:0,2:0}
        h=0
        for v in nums:
            d[v]+=1
        for i,j in d.items():
            for k in range(j):
                nums[h]=i
                h+=1
                
            
