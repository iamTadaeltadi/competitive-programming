class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=Counter(nums)
        operations=0
        for i in nums:
            if count[i]!=0 and k-i in count and count[k-i]!=0:
                if i!=k-i:
                    operations+=1
                    count[k-i]-=1
                    count[i]-=1
                else:
                    if count[i]>=2:
                        operations+=1
                        count[k-i]-=1
                        count[i]-=1



        return operations