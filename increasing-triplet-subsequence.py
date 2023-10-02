class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:


        remainingMaxNum=[]
        min_val=float("inf")
        max_val=float("-inf")
        for i in range(len(nums)-1,-1,-1):
            max_val=max(max_val,nums[i])
            # print(max_val)

            remainingMaxNum.append(max_val)
        print(remainingMaxNum)
        remainingMaxNum=remainingMaxNum[::-1]
            

        for i in range(len(nums)):
            if nums[i] >min_val and remainingMaxNum[i]>nums[i]:
                return True
            min_val=min(nums[i],min_val)
        return False