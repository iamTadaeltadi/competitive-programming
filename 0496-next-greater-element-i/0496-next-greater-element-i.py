class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        d={}
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                d[stack.pop()]=nums2[i]
            stack.append(nums2[i])
        print(d)
        for i in range(len(nums1)):
            if nums1[i] in d:
                nums1[i]=d[nums1[i]]
            else:
                nums1[i]=-1
        return nums1
            