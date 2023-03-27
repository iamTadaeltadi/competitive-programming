class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.nums1=nums1
        self.diff=diff
        self.nums2=nums2
        self.count=0
        self.res=[ nums1[i]-nums2[i] for i in range(len(nums1))]
        self.mergesort(0,len(nums1)-1)
        return self.count
        
    def mergesort(self,l,r):
        if l==r:
            return [self.res[l]]

        mid=(l+r)//2
        left=self.mergesort(l,mid)
        right=self.mergesort(mid+1,r)
        self.compare(left,right)

        return self.merge(left,right)
    def merge(self,left,right):
        
        l,r=0,0
        result=[]
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1
        while l<len(left):
            result.append(left[l])
            l+=1
        while r<len(right):
            result.append(right[r])
            r+=1
        return result
    def compare(self,left,right):
        
        # print(self.res)
        l=0
        for i in range(len(right)):
            while l<len(left) and left[l] <=right[i]+self.diff:
                l+=1
            
            self.count+=l
       