class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count=0
        def mergeSort(l,r):
            nonlocal count
            if l==r:
                return [nums[l]]
            mid=l+(r-l)//2
            left=mergeSort(l,mid)
            right=mergeSort(mid+1,r)
            l2=0
            for val in left:
                while l2 <len(right) and val>right[l2]*2:
                    l2+=1
                count+=l2
            result = []
            l, r = 0, 0
            while  l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1

            
            result += left[l:]
            result += right[r:]
            return result
        mergeSort(0,len(nums)-1)
        return count
                    
            
        
        
       
     
