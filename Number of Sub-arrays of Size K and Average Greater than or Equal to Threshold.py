class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, t: int) -> int:
        l,c=0,0
        s=(sum(nums[:k]))//k
        if s>=t:
            c+=1
        for r in range(k,len(nums)):
            s+=nums[r]/k
            s-=nums[l]/k
            print(s)
            if s>=t:
                c+=1
            l+=1
        return c
