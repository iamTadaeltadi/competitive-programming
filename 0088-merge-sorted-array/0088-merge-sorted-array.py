class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        store = []
        l , r = 0 , 0
        while l < m and r < n:
            if nums1[l] < nums2[r]:
                store.append(nums1[l])
                l += 1
            else:
                store.append(nums2[r])
                r += 1
        while l < m:
            store.append(nums1[l])
            l += 1
        while r < n:
            store.append(nums2[r])
            r += 1
        for i in range(len(store)):
            nums1[i] = store[i]
        
        
        