lass Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        num=[nums[0]]
        for i in range(1,len(nums)):
            num.append(num[-1]+nums[i])
        l,r=0,len(nums)-k-1
        v=[]
        print(num)
        while r<len(nums):
            if l==0:
                x=num[r]
            else:x=num[r]-num[l-1]
            v.append(x)
            l+=1
            r+=1
        vv=min(v)
        return sum(nums)-vv
