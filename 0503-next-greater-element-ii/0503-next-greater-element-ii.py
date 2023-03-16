class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[-1]*n
        stack=[]
        
        for index in range(2*n):
            index%=n #to avoid index out of bound iterates twice the loop
            while stack and stack[-1][0]<nums[index]:#to to create decresing monotonic stack
                result[stack.pop()[1]]=nums[index] # coming element popout prev smaller elmt and update 
                
            stack.append([nums[index],index]) #append the current element to stack with its index
            
        return result