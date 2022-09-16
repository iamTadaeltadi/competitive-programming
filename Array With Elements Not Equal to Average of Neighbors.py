def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        m=len(nums)//2
        mm=nums[:m]
        l=nums[m:]
        cc=0
        for i in range(1,len(nums),2):
            nums[i]=mm[cc]
            cc+=1
        n=0
        for i in range(0,len(nums),2):
            nums[i]=l[n]
            n+=1
        return nums



