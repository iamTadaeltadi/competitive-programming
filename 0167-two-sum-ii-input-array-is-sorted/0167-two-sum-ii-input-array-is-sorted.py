class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        n=len(numbers)
        right=len(numbers)-1
        while right<n :
            if numbers[left]+numbers[right]<target:
                left+=1
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                return [left+1,right+1]
                
                
            
        