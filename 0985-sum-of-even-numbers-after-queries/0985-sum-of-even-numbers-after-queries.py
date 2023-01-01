class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sum_of_even=0
        ans=[]
        for i in nums:
            if i%2==0:
                sum_of_even+=i
        for i,j in queries:
            if nums[j]%2==0:
                sum_of_even-=nums[j]
            val=nums[j]+i
            if val%2==0:
                sum_of_even+=val
            ans.append(sum_of_even)
            nums[j]=val
        return ans