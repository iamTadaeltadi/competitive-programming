class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l , r = m - 1 , n - 1
        index = len(nums1)-1
        while l >= 0 and r >= 0:
            if nums1[l] >= nums2[r]:
                nums1[index] = nums1[l]
                l -= 1
            else:
                nums1[index] = nums2[r]
                r -= 1
            index -= 1
            
        while l >= 0 and r < 0 :
                nums1[index] = nums1[l]
                l -= 1
                index -= 1
        while r >= 0 and l < 0 :
                nums1[index] = nums2[r]
                r -= 1
                index -= 1
        
                
                
        
            