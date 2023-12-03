class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        count = 1
        answer = set()
        n = len(nums)//3+1


        if n ==1:
            answer.add(nums[0])

        for i in range(1,len((nums))):

            

            if nums[i] == nums[i-1]:
                count+=1
            else:
                count = 1


            if count >= n:
                answer.add(nums[i])

            

        return list(answer) 