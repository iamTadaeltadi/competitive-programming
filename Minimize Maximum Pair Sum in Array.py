lass Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        c=-1
        s=[]
        for i in range(len(nums)//2):
            s.append((nums[i],nums[c]))
            c-=1
        m=0
        for i,j in s:
            m=max(i+j,m)
        return m
