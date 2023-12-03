class Solution:
    def findPeakElement(self, nums: List[int]) -> int:



        left = [nums[0]]


        for i in range(1,len(nums)):
            left.append(max(nums[i],(left[-1])))



        right = [nums[-1]]

        for i in range(len(nums)-2,-1,-1):
            right.append(max(nums[i],(right[-1])))
        

        l = 0
        r = len(nums) -1

        if len(nums) ==1:
            return 0
        
        right.reverse()

        print(left,right)

        while l<=r:
            mid = (l) +(r-l)//2
            print(mid)

            if mid>0 and mid <len(nums)-1 and nums[mid] >= left[mid-1] and nums[mid] >= right[mid+1]:
                return mid
            


            if mid ==0 and len(nums)>=2 and  nums[mid] >= right[mid+1] :
                print("x")
                return 0

            if mid == len(nums)-1 and len(nums)>=2 and  nums[mid] >= left[mid-1] :
                return len(nums)-1
            

            if mid ==0:
                print("x")
                l = mid+1
            
            elif mid == len(nums)-1 :
                r = mid -1
            elif nums[mid] < left[mid-1] >= right[mid+1] :
                r = mid-1

            elif nums[mid] < right[mid+1] >= left[mid-1] :
                l = mid +1

        
        return -1

    
            

            




        


        

       
        