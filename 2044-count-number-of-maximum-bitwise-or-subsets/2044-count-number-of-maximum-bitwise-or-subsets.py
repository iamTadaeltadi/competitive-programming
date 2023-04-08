class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_val=0
        for i in nums:
            max_val|=i
        count=0
        n=2**len(nums)-1
        print(n)

        for i in range(1,n+1):
            index=0
            val=0
            while i>0:
                if i&1==1:
                    val|=nums[index]
                            
                i>>=1
                index+=1
            if val==max_val:
                count+=1
        return count
        

                